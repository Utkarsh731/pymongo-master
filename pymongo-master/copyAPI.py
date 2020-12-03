import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGE0YmJjNmNlNDQ3NDgyODhjYjU1ZjY1MTE5MDdmN2MiLCJ0ZW5hbnQiOiJvbWxvZ2lzdGljcyIsIm5hbWUiOiJVdGthcnNoIHNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiYWQyNTU3YmFiMWM2NDJiYzgxM2I2MTI1NTVmZmNhNTMiLCJpc3MiOiJkNGRjYmYwZC0xNzUzLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM5NDg5ODksImV4cCI6MTYwNDEyODk4OX0.MZk9f8sKjMf2M41VhxfDPugo6Teb7vIK80tD_dBFUh8wzFSWt2RI8PXz2r_vMetz_60ThXXNmWzeOcgGTuPn-Q" ,"x-project-id":"192a853378514a9aad9d0f067169ebc5"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX1JPTEUiLCJrZXkiOiI3NWVhODNiNWViMWI0ZmU5OGU4YTVlNjFhNDQyMzk2NCIsImlzcyI6IjIxNGFhM2RlLTE5YzAtMTFlYi1hM2M0LTAyZjU3ODc2NGJmYSIsImlhdCI6MTYwMzk2NDM2NywiZXhwIjoxNjA0MTQ0MzY3fQ.a2veDUBdBYnnD-U4EjQHQKrpA8wE-yBWwEM3q1b7F-gE2Q_23yLu68Ejy-T0hBh7t6pIelA9ZYqMS4NA8OCPSQ','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://omlogistics.iot83.com/api/v2/gateway/api", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
print(dataFromMigrant[0])
count=0
for i in dataFromMigrant:
    print(i)
    apis=i.get("apis")
    payload={}
    for j in apis:
        try:
            payload["actionName"]=j["actionName"]
            payload["description"] = j["description"]
            payload["category"]=j["category"]
            payload["basePath"]=j["basePath"]
            payload["moduleName"]=j["moduleName"]
            payload["path"]=j["path"]
            payload["pathParameters"]=j["pathParameters"]
            payload["pathParameters"] = j["pathParameters"]
            payload["requestMethod"]=j["requestMethod"]
            postCall = requests.post("https://tracking.iot83.com/api/v2/gateway/api", json=payload,headers=headerForMigration, verify=False)
            count+=1
            print(count)
        except:
            print("error")

