#!/usr/bin/env python
import requests


url=raw_input("URL ")

xss_file = open("xsspayload.txt", "r")
xss_payload = xss_file.readlines()
xss_file.close()
index = url.find("=")
if "=" in url:
	for i in xss_payload:
		try:
               		i = i.split("\n")[0]
                	request = str(url[:index + 1]) + str(i)
                	content = requests.get(request)
                	print request
			if i in content.content:
                    		print "-"*50
				print "[+]XSS payload: ", str(i)
                   	        print "[+]XSS URL: ", request
                    
				print "-"*50
				print "-"*50
	
                	else:
                    		print "-"*50
				print "[-]XSS payload: ", str(i)
                    		print "[-]XSS URL: ", request
                except:
                        pass
else:
        print "[-]XSS Not Found"
