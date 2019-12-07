import requests
import json

header={"X-ApiKeys":"accessKey=XXXXX; secretKey=XXXXXXXX;"}

url="https://127.0.0.1:8834/scans/8"

sonuc=requests.get(url=url,headers=header,verify=False)
result=[]
a = sonuc.json()

for i in a["hosts"]:
	print "-"*50
	print "Up Host: ",i["hostname"]
	print "Info : ",i["info"]
	print "Low :",i["low"]
	print "Medium :",i["medium"]
	print "High :",i["high"]
	print "Critical :",i["critical"]
	print "-"*50


