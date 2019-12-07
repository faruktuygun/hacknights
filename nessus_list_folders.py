import requests
import json

header={"X-ApiKeys":"accessKey=XXXXXXXXX; secretKey=XXXXXXX;"}

url="https://127.0.0.1:8834/folders"

sonuc=requests.get(url=url,headers=header,verify=False)
result=[]
print sonuc.json()
for i in sonuc.json()['folders']:
	try:
		result.append(i)

	except:
		pass

for i in result:
	print "-"*50
	print "Name: ",i["name"]
	print "ID: ",i["id"]
	print "-"*50
