import os
import re
import requests
from urllib.parse import urlparse
from notion_client import Client
import uuid
import hashlib
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Export Notion pages to Markdown")
    parser.add_argument("database_id", help="Notion database ID")
    parser.add_argument("--output-dir", default="notion_export", help="Output directory for Markdown files")
    return parser.parse_args()

# Set up the Notion client with an environment variable or replace below
notion = Client(auth=os.getenv("NOTION_API_KEY"))  # or replace with 'auth="your-integration-token"'

# Helper: Slugify file names
def slugify(text):
    return re.sub(r'[^\w\- ]+', '', text).strip().lower().replace(' ', '-')

# Helper: Extract Notion text
def extract_text(rich_text):
    return ''.join([t["text"]["content"] for t in rich_text])

# Helper: Download image to local folder
def download_image(url, output_dir, filename_hint="image"):
    os.makedirs(output_dir, exist_ok=True)

    # Generate a short unique hash from the URL or a UUID
    unique_id = hashlib.md5((url + str(uuid.uuid4())).encode()).hexdigest()[:8]

    parsed_url = urlparse(url)
    ext = os.path.splitext(parsed_url.path)[-1]
    ext = ext if ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp'] else '.png'

    filename = f"{filename_hint}-{unique_id}{ext}"
    filepath = os.path.join(output_dir, filename)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
        else:
            print(f"⚠️ Failed to download image: {url}")
    except Exception as e:
        print(f"⚠️ Error downloading image: {e}")
    return None

# Helper: Fetch all child blocks (recursive pagination)
def get_block_children(block_id):
    blocks = []
    start_cursor = None
    while True:
        response = notion.blocks.children.list(block_id, start_cursor=start_cursor)
        blocks.extend(response['results'])
        if not response.get('has_more'):
            break
        start_cursor = response['next_cursor']
    return blocks

# Convert a block to Markdown
def block_to_markdown(block, image_dir):
    type = block["type"]
    content = block[type]

    if type == "paragraph":
        return extract_text(content["rich_text"]) + "\n"

    elif type == "heading_1":
        return "# " + extract_text(content["rich_text"]) + "\n"

    elif type == "heading_2":
        return "## " + extract_text(content["rich_text"]) + "\n"

    elif type == "heading_3":
        return "### " + extract_text(content["rich_text"]) + "\n"

    elif type == "bulleted_list_item":
        return "- " + extract_text(content["rich_text"]) + "\n"

    elif type == "numbered_list_item":
        return "1. " + extract_text(content["rich_text"]) + "\n"

    elif type == "to_do":
        checked = content.get("checked", False)
        box = "[x]" if checked else "[ ]"
        return f"- {box} {extract_text(content['rich_text'])}\n"

    elif type == "code":
        text = extract_text(content["rich_text"])
        language = content.get("language", "")
        return f"```{language}\n{text}\n```\n"

    elif type == "quote":
        return "> " + extract_text(content["rich_text"]) + "\n"

    elif type == "callout":
        return f"> 💡 {extract_text(content['rich_text'])}\n"

    elif type == "image":
        if content["type"] == "external":
            url = content["external"]["url"]
        else:
            url = content["file"]["url"]

        caption = extract_text(content.get("caption", []))
        alt_text = caption or "Image"

        filename_hint = slugify(alt_text) or "notion-image"
        local_path = download_image(url, output_dir=image_dir, filename_hint=filename_hint)

        if local_path:
            rel_path = os.path.relpath(local_path, "notion_export")
            return f"![{alt_text}]({rel_path})\n"
        else:
            return f"![{alt_text}]({url})\n"

    else:
        return f"<!-- Unsupported block type: {type} -->\n"

# Extract Markdown from a full Notion page
def notion_page_to_markdown(page_id, image_dir):
    md_lines = []
    blocks = get_block_children(page_id)

    for block in blocks:
        md = block_to_markdown(block, image_dir)
        md_lines.append(md)

        # Recursively include children
        if block.get("has_children"):
            children = get_block_children(block["id"])
            for child in children:
                md_lines.append("  " + block_to_markdown(child, image_dir))

    return "".join(md_lines)

# Extract title of the page
def get_page_title(page):
    props = page.get("properties", {})
    for prop in props.values():
        if prop["type"] == "title":
            return extract_text(prop["title"])
    return "untitled"

# Export all pages in a Notion database
def export_database_to_markdown(database_id, output_dir="notion_export"):
    

    os.makedirs(output_dir, exist_ok=True)
    image_dir = os.path.join(output_dir, "images")
    start_cursor = None

    while True:
        response = notion.databases.query(database_id=database_id, start_cursor=start_cursor)
        for page in response["results"]:
            page_id = page["id"]
            title = get_page_title(page)
            filename = slugify(title) or page_id[:8]

            markdown = notion_page_to_markdown(page_id, image_dir)

            filepath = os.path.join(output_dir, f"{filename}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(markdown)

            print(f"✅ Exported: {title} → {filepath}")

        if not response.get("has_more"):
            break
        start_cursor = response["next_cursor"]

def main():
    args = get_args()
    database_id = args.database_id
    output_dir = args.output_dir

    export_database_to_markdown(database_id, output_dir)


# Entry point
if __name__ == "__main__":
    main()
