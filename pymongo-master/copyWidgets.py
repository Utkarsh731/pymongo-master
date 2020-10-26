import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJVdGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODczY2IxODUyNjBlNDRhOTllNjFlZGIzYWM1MzY0ZTYiLCJ0ZW5hbnQiOiJibWNzb2Z0d2FyZSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFVkVMT1BFUiIsImtleSI6ImU3Y2JmNGIwNzQ5YTQzNmZiYjNiMjMyNTQyZjA1MjllIiwiaXNzIjoiNTY5NDAxZjEtMGM0Ny0xMWViLWEzYzQtMDJmNTc4NzY0YmZhIiwiaWF0IjoxNjAzNjg4MzE0LCJleHAiOjE2MDM4NjgzMTR9.FJhDuf-4s5X4DaiwO7E-KzQGG0wkWR799JCJJFY4SJ7i5p2IK1KjJPYZLCRCCF5YaEcgxtVpgZRzNm6E6SsmJQ" ,"x-project-id":"dc3c1c4749334ce4b27401efffefee8b"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGE0YmJjNmNlNDQ3NDgyODhjYjU1ZjY1MTE5MDdmN2MiLCJ0ZW5hbnQiOiJvbWxvZ2lzdGljcyIsIm5hbWUiOiJVdGthcnNoIHNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjBmMjJlZWM4YTE5NDlkN2I3NWJiNTRiZTZkYzY5MjciLCJpc3MiOiJkNGRjYmYwZC0xNzUzLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM2OTM3NzEsImV4cCI6MTYwMzg3Mzc3MX0.wKQMcKcYK_iZ5AQtKedlMVWTlYw77jUOfdXnfnUNh6r8wjDDduiFTGZOSYefpBqa9cvnaDHP4MbN3we_teaEdA','x-project-id':'192a853378514a9aad9d0f067169ebc5'}
responseFromMigrant=requests.get("https://bmcsoftware.iot83.com/api/v2/widgets?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=0
for i in dataFromMigrant:
    responseCodeFromMigrant=requests.get("https://bmcsoftware.iot83.com/api/v2/widgets/"+i["id"], headers=headerForMigrant, verify=False).json().get('data')
    dataSet=responseCodeFromMigrant.get("data")
    subCategory=responseCodeFromMigrant.get("subCategory")
    widgetDisplayName=responseCodeFromMigrant.get("widgetDisplayName")
    widgetName=responseCodeFromMigrant.get("widgetName")
    widgetSettings=responseCodeFromMigrant.get("widgetSettings")
    widgetsList=responseCodeFromMigrant.get("widgetsList")
    payload={"category":"customWidgets","categoryDisplayName":"Custom Widgets","categoryIcon":"fad fa-image-polaroid","categoryImageName":None,"data":dataSet,"description":i["description"],"disabled":False,"icon":None,"imageName":"html.png","subCategory":subCategory,"widgetDisplayName":widgetDisplayName,"widgetName":widgetName,"widgetSettings":widgetSettings,"widgetsList":widgetsList}
    try:
        postCall = requests.post("https://omlogistics.iot83.com/api/v2/widgets?pushToGit=false", json=payload,headers=headerForMigration, verify=False)
        count += 1
        print(count)
        print(postCall.text)
    except:
        print("error")
