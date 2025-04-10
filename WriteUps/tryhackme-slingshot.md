# TryHackMe-Slingshot

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/680fc2cc-5dcb-4f41-8833-a9845fe19aa3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLT6QVSW%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIDJbT3Jsa4EsrjZP75IQhQuv6uvkLXUiG80mJPuOxE4QAiEA2yJkYLyFdecC4yWoad4VMp43N%2BVN8Ifuh8N0Jr7%2Bcu4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNrDZ2BKHeyk0lgGYSrcA3SAAXkljLXVYsi74H745zisqJde6HgdzYkM1e%2F7%2BCxcqgqpmIRrTSGTN5v1%2BZ2yXisdRmixA3SjEPBgt2M%2Frq5WgsX6fEvmjNgJdgfJVzoatIEYyc9qzJG126f0PoLev3Xmq2tMoA1PhQpzfHMjEKXgXb02lfeMuT%2BQlXtEJJ0K0aLX1rVo4QWMSGwa7uyjtGsSdWyw5FdiXvxtQIVU5IVX9V92ErAaTSjY%2FEheHzeDFqtjFRH9%2Bsw4YDjrauD%2Fx%2BNvvDA6DaogwfEtktdVBmM7v7WWOLwHGabiaukma%2FPlpVoOnVTsYrWWoU6KuEXNGoSnhOxwnZ4r5js%2BfwzH%2FZmdDPc8Zzz%2F9MOb%2FLsGJ3G1BOQwD5msiaDRNUVu51AXhoo%2BMDBpB5R6QNMjt0yhFfxuIiDajALpx7COseM9TnFE5wnDnZeqwgOz7qSeKju8McIsJ%2FTqryE%2BUa6ovRyIqYrHlElIZ03zL4zzvsRWVyF0%2FX5C21RrnqTO%2Fs9NRWPFEVKPujYTmdGKwzsDn5VOxxmLhdHeV2GUI9ePUcaavSny27DLW9pYGD0G2lE%2BUXT6iKKqCvUMN1YRyraUsVdVcrPcIyDB%2FFg06TWSLwGK7OSqMoy9H5DVLYZ%2B9v9NMLGf4L8GOqUBOzSJfo9pdYKax8mZ6UA0erc1xT8ht9ET7Px0Kx3KgLxaZYsEJm55hJCzgnLjBxs%2BOBouDIBdoIrlZz9Oltz6cYDUIyDifcc4wpH%2BVXEo3w7NgUu%2Bqlp4RWbViLDeF33Jr%2F%2BnMXm7g%2B9b6%2FtpdIkdUSLJUffJzkPryF0slXVkPyVQq22nRRwKvYo5muXAkoqwVZprzDKbM2RAulUAX9s6mzLtFPht&X-Amz-Signature=37931eb32764c227f8d827778c8f310d691210f610913adc30dc877fa3cfaf18&X-Amz-SignedHeaders=host&x-id=GetObject)
# TryHackMe - Slingshot Writeup
# Background
Slingway Inc., a leading toy company, has recently noticed suspicious activity on its e-commerce web server and potential modifications to its database. To investigate the suspicious activity, they've hired you as a SOC Analyst to look into the web server logs and uncover any instances of malicious activity.
To aid in your investigation, you've received an Elastic Stack instance containing logs from the suspected attack. Below, you'll find credentials to access the Kibana dashboard. Slingway's IT staff 
mentioned that the suspicious activity started on July 26, 2023.
By investigating and answering the questions below, we can create a timeline of events to lead the incident response activity. This will also allow us to present concise and confident findings that answer questions such as:
- What vulnerabilities did the attacker exploit on the web server?
- What user accounts were compromised?
- What data was exfiltrated from the server?

# Investigation




# Questions
What was the attacker's IP?

What was the first scanner that the attacker ran against the web server?

What was the User Agent of the directory enumeration tool that the attacker used on the web server?

In total, how many requested resources on the web server did the attacker fail to find?

What is the flag under the interesting directory the attacker found?

What login page did the attacker discover using the directory enumeration tool?

What was the user agent of the brute-force tool that the attacker used on the admin panel?

What username:password combination did the attacker use to gain access to the admin page?

What flag was included in the file that the attacker uploaded from the admin directory?

What was the first command the attacker ran on the web shell?

What file location on the web server did the attacker extract database credentials from using Local File Inclusion?

What directory did the attacker use to access the database manager?

What was the name of the database that the attacker exported?

What flag does the attacker insert into the database?
