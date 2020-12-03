import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiYjMzMmMwYjVlMzgzNGFkYWE3ZDMxYjM5N2RlZGMxMjciLCJ0ZW5hbnQiOiJkZW1vc2FsZXMiLCJuYW1lIjoiVXRrYXJzaCBTaHVrbGEiLCJpc1ZlcmlmaWVkIjp0cnVlLCJpc0xpY2Vuc2VFeHBpcmVkIjpmYWxzZSwiaW50ZXJuYWxVc2VyIjp0cnVlLCJyb2xlIjoiQkFDS0VORF9ERVZFTE9QRVIiLCJrZXkiOiIwOTE0MDcxNTVhMWI0ZjVhYWQ1MWI3N2EzNTMwNTVlZCIsImlzcyI6IjQ4ZGVhNTc4LTc5YmQtMTFlYS1hM2M0LTAyZjU3ODc2NGJmYSIsImlhdCI6MTYwNTY3NDkyMSwiZXhwIjoxNjA1ODU0OTIxfQ.chjtmh3uHd_PY1C0tl5_60PhPT62EkobEiMe2jpgYMrWln_wzxewR8EPF1EAss-NrzBs6WkjZqTRJ-d0H5zmqw" ,"x-project-id":"cc810a2fe23f4774beeaac89ad3a4220"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiNzY2ODIyNjYwMTcyNGZhODk2ZjAyOGJjYWZjNmUwNTAiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDU2NzY1OTEsImV4cCI6MTYwNTg1NjU5MX0.xqiGpmoeASOPLMqTwaWjZ1_lJTT24DPQlMPVNnrQv-ssgey14e8Qx-U53m3mjIfFpKaimpX-T7GuCcGvwDwShQ','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://demosales.iot83.com/api/v2/widgets?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=0
for i in dataFromMigrant:
    responseCodeFromMigrant=requests.get("https://demosales.iot83.com/api/v2/widgets/"+i["id"], headers=headerForMigrant, verify=False).json().get('data')
    dataSet=responseCodeFromMigrant.get("data")
    subCategory=responseCodeFromMigrant.get("subCategory")
    widgetDisplayName=responseCodeFromMigrant.get("widgetDisplayName")
    widgetName=responseCodeFromMigrant.get("widgetName")
    widgetSettings=responseCodeFromMigrant.get("widgetSettings")
    widgetsList=responseCodeFromMigrant.get("widgetsList")
    payload={"category":"customWidgets","categoryDisplayName":"Custom Widgets","categoryIcon":"fad fa-image-polaroid","categoryImageName":None,"data":dataSet,"description":i["description"],"disabled":False,"icon":None,"imageName":"html.png","subCategory":subCategory,"widgetDisplayName":widgetDisplayName,"widgetName":widgetName,"widgetSettings":widgetSettings,"widgetsList":widgetsList}
    try:
        postCall = requests.post("https://tracking.iot83.com/api/v2/widgets?pushToGit=true&commitMessage=Testing", json=payload,headers=headerForMigration, verify=False)
        count += 1
        print(count)
    except:
        print("error")
