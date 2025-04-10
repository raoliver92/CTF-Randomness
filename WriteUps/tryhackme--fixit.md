# TryHackMe- Fixit

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/7e760d56-fca9-4231-91aa-030ccc06e17d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=2f2d2b63116eed7ebf49990609d44240cd7c988b2c93c300b4e7410258758bcb&X-Amz-SignedHeaders=host&x-id=GetObject)
# TryHackMe - Fixit Writeup
# Background
In this challenge room, you will act as John, who has recently cleared his third screening interview for the SOC-L2 position at MSSP Cybertees Ltd, and a final challenge is ready to test your knowledge, where you will be required to apply the knowledge to FIX the problems in Splunk.
You are presented with a Splunk Instance and the network logs being ingested from an unknown device.
# Challenge: FIXIT
This challenge is divided into three levels:
### Level 1: Fix Event Boundaries
Fix the Event Boundaries in Splunk. As the image below shows, Splunk cannot determine the Event boundaries, as the events are coming from an unknown device.
![Image](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e8dd9a4a45e18443162feab/room-content/6e62548849068f986f25d9d0c8f52c9c.png)
### Level 2: Extract Custom Fields
Once the event boundaries are defined, it is time to extract the custom fields to make the events searchable.
- Username
- Country
- Source_IP
- Department
- Domain
Sample Logs:
To create regex patterns, sample Network logs are shown below:
```c
[Network-log]: User named Johny Bil from Development department accessed the resource Cybertees.THM/about.html from the source IP 192.168.0.1 and country
Japan at: Thu Sep 28 00:13:46 2023
[Network-log]: User named Johny Bil from Marketing department accessed the resource Cybertees.THM/about.html from the source IP 192.168.2.2 and country
Japan at: Thu Sep 28 00:13:46 2023
[Network-log]: User named Johny Bil from HR department accessed the resource Cybertees.THM/about.html from the source IP 10.0.0.3 and country
Japan at: Thu Sep 28 00:13:46 2023
```
Level 3: Perform Analysis on the FIXED Events
Once the custom fields are parsed, we can use those fields to analyze the Event logs. Examine the events and answer the questions.
Happy Fixing!


# Fixing Event Boundaries
From above, the event boundaries are not being parsed correctly and causing line breaks at abnormal locations in the logs. This is due to a missing or misconfiguration in the props.conf file.
Looking into the default directory within the fixit app, I noticed that there isn’t a props.conf defined which is the cause of the weird line breaks. 
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/308af973-e1a2-4770-9485-04e8c3d3f3e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=b3f170240f70a58ed37f22c42a09d8778cbde6d263bbb23acaac5b18b3616bae&X-Amz-SignedHeaders=host&x-id=GetObject)
This can be fixed by creating the file and adding the below configurations to the sourcetype which is defined in the inputs.conf for the network logs.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/bd353dc2-e745-4af9-8e2f-77593919c6b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=ec5c63490cea4a53ce04970fea85d64d42aeaa60e16aff2779942ecc90fdd9c1&X-Amz-SignedHeaders=host&x-id=GetObject)
```javascript
[network_logs]
SHOULD_LINEMERGE = true
BREAK_ONLY_BEFORE = \[Network-log\]
```
After restarting splunk we can see that the logs are being parsed correctly with linebreaks at each new log.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/fd3b0eeb-d96a-4e11-bb6f-a44b40a67780/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=ccfcca44a16f235a0fe1a5768dddca0683a54323ddaa4f319495a33ac0fb8a33&X-Amz-SignedHeaders=host&x-id=GetObject)

# Extracting Custom Fields
To extract the custom fields I used regex101.com to test out the regex needed to extract the fields and then added that to the respective conf files below.
- Username
- Country
- Source_IP
- Department
- Domain
Regex I came up with to extract the fields is as such. I don’t claim to be good at regex but it worked. I’m sure there are better ways for performance to extract these fields.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/ceab7a01-736e-48e7-803e-2ef716299074/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=804763fcbf9162b360fcdacc73bd85ead44e56edb975a6e832fdf86ed41c8839&X-Amz-SignedHeaders=host&x-id=GetObject)
```javascript
named\s(\w+\s.\w+)\sfrom\s(\w+).+resource\s(\w+\.\w+).+IP\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+country\s\n(\w.+)\sat
```
transforms.conf
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/1c1436cf-5d9c-452f-8c73-25b9c4ca8aff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=8f40bff444f6b55f52694242039a863fd3bb285cf8bd2c39158cda85ae853d58&X-Amz-SignedHeaders=host&x-id=GetObject)
fields.conf
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/1d486f66-30b4-4d99-84dd-ef89c5eac6fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=4ca1e090d99237cd1e75381f30591d88add955f772a533925468774928a8f8f9&X-Amz-SignedHeaders=host&x-id=GetObject)

props.conf
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/662b8103-bd0d-4c9f-9487-f39a3cdf3ede/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=fd39683cbc6f33160c63c53d3f206b1d123cf2e6730aa5ff6745f53197665f04&X-Amz-SignedHeaders=host&x-id=GetObject)

After restarting the splunk server and running the search again I can see the fields are being broken out as expected within each event.
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/6a605c0f-086c-4154-ba2d-e3fba2bb7992/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=f1428a5d0e8ec37d80e121379a7d5b09a721a56f27e5070bb563785acdc1f68e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/2dc1c374-4060-41d0-87aa-77071f8288e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=6d83d217697f983a107c728cc7313f185d23a321faadf0afdae440a518459a16&X-Amz-SignedHeaders=host&x-id=GetObject)

### What is the full path of the FIXIT app directory?
This app can be found in /opt/splunk/etc/apps/
### What Stanza will we use to define Event Boundary in this multi-line Event case?
[Network-log] starts every event so we can use the BREAK_ONLY_BEFORE 
### In the inputs.conf, what is the full path of the network-logs script?
This can be found by looking inside of /opt/splunk/etc/apps/fixit/default/inputs.conf

### What regex pattern will help us define the Event's start?
\[Network-log\]
### What is the captured domain?
![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/0cfa02cd-92e7-492f-8163-1d853193c777/e6ca6a5f-4913-4c93-a3c6-faebc92d1501/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636W7CKBG%2F20250410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250410T184019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCICXzEiVcEp38lUCtZy1z7x5YOsbjp4Ofm0VsmMwazvLdAiEAs4awMcfoXWLZd4TnqwOxs0V3NdHzyOr8zouWvQSFYgUqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIb8hTD2KBqvnyxYsyrcA%2BgL%2BrEnfrNkjlrDREQdsib9imf4Q5aOCGtaaZCvW0XuXwGIZFmX4eT%2BRQ43zNgFHi7Ie2lfG9gFZGbFd2pI7OVRz0TgDO2iy4ZJaw4ydNaGc6gTaKfkytYGpfgcZIatZQPs13C%2B4bjeT4iDXJ1E3ElNvKxAkzWvZOc2nOA4IiuG3E6LMB%2BXJzIVTgm3%2B8KeWUR9z%2FleV7T7fWzCHNt%2BbjEM46NYutciDUc5Y471ghJPsNv6p%2BYLvzMDBH2ODOSF9m1%2F0AJ09qxXCwJ86gkkxOY4sc%2B6ShX4rAs19MriQjT4exVWTNM5hLI%2FPrzBeZtNpowf8AlozbcD%2BYB%2BXCa67yw4%2FwO1nU5v3ACSupjTLPD6fFqZMp4ld8VDsDjVIM8LyNQlKhrXM92D%2BDTeG%2FjXEBL55F9BWLYjdLat3bpTsAsvgzbWOJc%2FoXqJk%2FU2QZNM0Z9QvGbiNAdqN9xCOG%2BuvKg1QHydstRQ8gg5rngy%2BYHYU%2Bbds0ALaBGzkLCTVnGWLdLqFLTQ2d0DE4T8QXruxvP%2BdY0Axu0GhAV9iDRCMufRhMEwAU4wsRsC0kYvznaCwXYixaER%2FMUDysgJqZQb1ywnbHc%2B6OFa6CUBLUH8d5MkCrrgiCWOOccifzAqMNWf4L8GOqUBG%2BMO2g64fHjT5uKIUwm%2BuyFParZ3Md4A5k3lQDQDFGNxWsIK81vtuAEFio%2B34kkyRDLaruR5bu5fj%2FIxV4XQN%2FqulMmt1JofRHjoFocHZSKWHkOY1zEUOItAaNlfUd7mTPhM%2FnIbbtUsmHi9ut7796y5tIGMeJOaoU47G4pSaHdjnmTclRIeNRBG%2FNd7nOOMHQyGmfp8lAMv5O79uyPLROl1vm9L&X-Amz-Signature=97e0dfbe544a04737c0228ff7fcb35cf775cacf12a59a7b66abe34f765428331&X-Amz-SignedHeaders=host&x-id=GetObject)
### How many countries are captured in the logs?
```javascript
index=main
|stats count by Country
```
### How many departments are captured in the logs?
```javascript
index=main
|stats count by Department
```
### How many usernames are captured in the logs?
```javascript
index=main
|stats count by Username
```
### How many source IPs are captured in the logs?
```javascript
index=main
|stats count by Source_IP
```
### Which configuration files were used to fix our problem? [Alphabetic order: File1, file2, file3]
Files can be found in /opt/splunk/etc/apps/fixit/default/
### What are the TOP two countries the user Robert tried to access the domain from? [Answer in comma-separated and in Alphabetic Order][Format: Country1, Country2]
```javascript
index=main Username=Robert*
|stats count by Country
|sort - count
```
### Which user accessed the secret-document.pdf on the website?
```javascript
index=main secret-document.pdf
|stats count by Username
```



