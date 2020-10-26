import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJVdGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODczY2IxODUyNjBlNDRhOTllNjFlZGIzYWM1MzY0ZTYiLCJ0ZW5hbnQiOiJibWNzb2Z0d2FyZSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFVkVMT1BFUiIsImtleSI6ImU3Y2JmNGIwNzQ5YTQzNmZiYjNiMjMyNTQyZjA1MjllIiwiaXNzIjoiNTY5NDAxZjEtMGM0Ny0xMWViLWEzYzQtMDJmNTc4NzY0YmZhIiwiaWF0IjoxNjAzNjg4MzE0LCJleHAiOjE2MDM4NjgzMTR9.FJhDuf-4s5X4DaiwO7E-KzQGG0wkWR799JCJJFY4SJ7i5p2IK1KjJPYZLCRCCF5YaEcgxtVpgZRzNm6E6SsmJQ" ,"x-project-id":"dc3c1c4749334ce4b27401efffefee8b"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGE0YmJjNmNlNDQ3NDgyODhjYjU1ZjY1MTE5MDdmN2MiLCJ0ZW5hbnQiOiJvbWxvZ2lzdGljcyIsIm5hbWUiOiJVdGthcnNoIHNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjBmMjJlZWM4YTE5NDlkN2I3NWJiNTRiZTZkYzY5MjciLCJpc3MiOiJkNGRjYmYwZC0xNzUzLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM2OTM3NzEsImV4cCI6MTYwMzg3Mzc3MX0.wKQMcKcYK_iZ5AQtKedlMVWTlYw77jUOfdXnfnUNh6r8wjDDduiFTGZOSYefpBqa9cvnaDHP4MbN3we_teaEdA','x-project-id':'192a853378514a9aad9d0f067169ebc5'}
responseFromMigrant=requests.get("https://bmcsoftware.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
responseFromMigration=requests.get("https://omlogistics.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigration, verify=False)
codeFromMigrant=responseFromMigrant.json().get("data")
codeFromMigration=responseFromMigration.json().get("data")
faas1,faas2=[],[]
for i in codeFromMigrant:
    faas1.append(i["actionName"])
for i in codeFromMigration:
    faas2.append(i["actionName"])
rejected=[]
for i in faas1:
 if i  in faas2:
     rejected.append(i)
print(rejected)