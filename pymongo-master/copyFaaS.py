import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGE0YmJjNmNlNDQ3NDgyODhjYjU1ZjY1MTE5MDdmN2MiLCJ0ZW5hbnQiOiJvbWxvZ2lzdGljcyIsIm5hbWUiOiJVdGthcnNoIHNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiYWQyNTU3YmFiMWM2NDJiYzgxM2I2MTI1NTVmZmNhNTMiLCJpc3MiOiJkNGRjYmYwZC0xNzUzLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM5NDg5ODksImV4cCI6MTYwNDEyODk4OX0.MZk9f8sKjMf2M41VhxfDPugo6Teb7vIK80tD_dBFUh8wzFSWt2RI8PXz2r_vMetz_60ThXXNmWzeOcgGTuPn-Q" ,"x-project-id":"192a853378514a9aad9d0f067169ebc5"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX1JPTEUiLCJrZXkiOiI3NWVhODNiNWViMWI0ZmU5OGU4YTVlNjFhNDQyMzk2NCIsImlzcyI6IjIxNGFhM2RlLTE5YzAtMTFlYi1hM2M0LTAyZjU3ODc2NGJmYSIsImlhdCI6MTYwMzk2NDM2NywiZXhwIjoxNjA0MTQ0MzY3fQ.a2veDUBdBYnnD-U4EjQHQKrpA8wE-yBWwEM3q1b7F-gE2Q_23yLu68Ejy-T0hBh7t6pIelA9ZYqMS4NA8OCPSQ','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://omlogistics.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=0
for i in dataFromMigrant:
    responseCodeFromMigrant=requests.get("https://omlogistics.iot83.com/api/v2/actions/"+i.get("id"), headers=headerForMigrant, verify=False)
    codeFromMigrant=responseCodeFromMigrant.json().get("data")
    code=codeFromMigrant["code"].replace("1929ebc5","537987b1")
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
        postCall=requests.post("https://tracking.iot83.com/api/v2/actions?pushToGit=true&commitMessage=testing",json=payload,headers=headerForMigration,verify=False)
        count+=1
        print(count)
    except:
        print("error")