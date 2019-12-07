#!/usr/bin/env python

import requests
import subprocess

subprocess.call('clear',shell=True)
directory=[]
IP=raw_input(" IP Address: ")
wordlst=raw_input(" Worlist Directory: ")
with open(wordlst,'r') as f:
    content = f.readlines()
for i in content:
    content = i.strip()
    directory.append(content)
f.close()
print ("-"*75)
for i in directory:
	url = "http://IP/read_data"
     	url = url.replace("read_data",i)     
     	url = url.replace("IP",IP)
        req = requests.get(url)
        if req.status_code == 200:
            print "[+] Found : ",url, "       Status Code:  " ,req.status_code 
            print ("-"*75)

