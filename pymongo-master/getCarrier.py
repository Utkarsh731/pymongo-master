import requests
header={"Authorization":"Basic QUMyYmI1YTMwODMzZjdhNDY5MzE2ZjAxMTcyMzhiZjMyMjo4Nzk4ODI1M2ViOTFiYWFlNjFmZDM0ZjU0OGQyMGNiNQ=="}
res=requests.get("https://lookups.twilio.com/v1/PhoneNumbers/+919582310408?Type=carrier",headers=header)
res=res.json()
print(res.get('carrier').get('name'))