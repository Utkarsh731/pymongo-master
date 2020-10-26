import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJVdGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODczY2IxODUyNjBlNDRhOTllNjFlZGIzYWM1MzY0ZTYiLCJ0ZW5hbnQiOiJibWNzb2Z0d2FyZSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFVkVMT1BFUiIsImtleSI6ImU3Y2JmNGIwNzQ5YTQzNmZiYjNiMjMyNTQyZjA1MjllIiwiaXNzIjoiNTY5NDAxZjEtMGM0Ny0xMWViLWEzYzQtMDJmNTc4NzY0YmZhIiwiaWF0IjoxNjAzNjg4MzE0LCJleHAiOjE2MDM4NjgzMTR9.FJhDuf-4s5X4DaiwO7E-KzQGG0wkWR799JCJJFY4SJ7i5p2IK1KjJPYZLCRCCF5YaEcgxtVpgZRzNm6E6SsmJQ" ,"x-project-id":"dc3c1c4749334ce4b27401efffefee8b"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGE0YmJjNmNlNDQ3NDgyODhjYjU1ZjY1MTE5MDdmN2MiLCJ0ZW5hbnQiOiJvbWxvZ2lzdGljcyIsIm5hbWUiOiJVdGthcnNoIHNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjBmMjJlZWM4YTE5NDlkN2I3NWJiNTRiZTZkYzY5MjciLCJpc3MiOiJkNGRjYmYwZC0xNzUzLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM2OTM3NzEsImV4cCI6MTYwMzg3Mzc3MX0.wKQMcKcYK_iZ5AQtKedlMVWTlYw77jUOfdXnfnUNh6r8wjDDduiFTGZOSYefpBqa9cvnaDHP4MbN3we_teaEdA','x-project-id':'192a853378514a9aad9d0f067169ebc5'}
responseFromMigrant=requests.get("https://bmcsoftware.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=32
for i in dataFromMigrant:
    responseCodeFromMigrant=requests.get("https://bmcsoftware.iot83.com/api/v2/actions/"+i.get("id"), headers=headerForMigrant, verify=False)
    codeFromMigrant=responseCodeFromMigrant.json().get("data")
    code=codeFromMigrant["code"].replace("dc3fee8b","1929ebc5")
    imageName=codeFromMigrant.get("imageName")
    overwrite=None
    requirements=[]
    actionName=i.get("actionName")
    description=i.get("description")
    imageDescription=i.get("imageDescription")
    kind=i.get("kind")
    pathParameters=i.get("pathParameters")
    memory=str(codeFromMigrant.get("memory"))
    responseFormat={}
    payload={"actionName":actionName,"category":"customWidgets","code":code,"description":description,"developmentMode":False,"imageDescription":imageDescription,"imageName":imageName,"kind":kind,"memory":memory,"overwrite":overwrite,"pathParameters":pathParameters,"requirements":requirements,"responseFormat":responseFormat,"saveAsDraft":False}
    try:
        postCall=requests.post("https://omlogistics.iot83.com/api/v2/actions?pushToGit=false",json=payload,headers=headerForMigration,verify=False)
        count+=1
        print(count)
    except:
        print("error")

