import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiYjMzMmMwYjVlMzgzNGFkYWE3ZDMxYjM5N2RlZGMxMjciLCJ0ZW5hbnQiOiJkZW1vc2FsZXMiLCJuYW1lIjoiVXRrYXJzaCBTaHVrbGEiLCJpc1ZlcmlmaWVkIjp0cnVlLCJpc0xpY2Vuc2VFeHBpcmVkIjpmYWxzZSwiaW50ZXJuYWxVc2VyIjp0cnVlLCJyb2xlIjoiQkFDS0VORF9ERVZFTE9QRVIiLCJrZXkiOiJiMjlkZGY0ZTUzNWE0NGJhODMzOTI0YzdkMmM4ZTYxNCIsImlzcyI6IjQ4ZGVhNTc4LTc5YmQtMTFlYS1hM2M0LTAyZjU3ODc2NGJmYSIsImlhdCI6MTYwMjQxNzM2NSwiZXhwIjoxNjAyNTk3MzY1fQ.WWaxxleFEmumsE6xfhPCVKqNJ5wG1rTj7Om1LlH07qPCSwzhHxw-rzbeL8_BiZITxTReBSHK8j11ZQ55km_vtw" ,"x-project-id":"cc810a2fe23f4774beeaac89ad3a4220"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJVdGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODczY2IxODUyNjBlNDRhOTllNjFlZGIzYWM1MzY0ZTYiLCJ0ZW5hbnQiOiJibWNzb2Z0d2FyZSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiYjI5YWEzNWQ4NTg1NGU2MDgwNDZlNTNkMzExODJiMDQiLCJpc3MiOiI1Njk0MDFmMS0wYzQ3LTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDI0ODQ5NjgsImV4cCI6MTYwMjY2NDk2OH0.AYVqTyS85tBsq3AzB39BiC_eqzam4Dk7E5wfi6a55iE99sXkDcrsP7nN8a7QMxQt3qHdFHIl2IvA_hYJv_8aKQ','x-project-id':'dc3c1c4749334ce4b27401efffefee8b'}
responseFromMigrant=requests.get("https://demosales.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
responseFromMigration=requests.get("https://bmcsoftware.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigration, verify=False)
codeFromMigrant=responseFromMigrant.json().get("data")
codeFromMigration=responseFromMigration.json().get("data")
faas1,faas2=[],[]
for i in codeFromMigrant:
    faas1.append(i["actionName"])
for i in codeFromMigration:
    faas2.append(i["actionName"])
rejected=[]
for i in faas1:
 if i not in faas2:
     rejected.append(i)
print(rejected)