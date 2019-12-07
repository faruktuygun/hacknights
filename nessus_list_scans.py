import requests
import json

header={"X-ApiKeys":"accessKey=XXXXXX; secretKey=XXXXXXX;"}

url="https://127.0.0.1:8834/scans"

sonuc=requests.get(url=url,headers=header,verify=False)
result=[]
print sonuc.json()
for i in sonuc.json()['scans']:
	if i["folder_id"]!=2:
		try:
			result.append(i)
		except:
			pass

for i in result:
	print "-"*50
	print "Name: ",i["name"]
	print "Status: ",i["status"]
	print "ID: ",i["id"]
	print "-"*50
