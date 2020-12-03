import requests,json
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiNWYyNDk1NDdkYjM4NGUxNDlkN2UwYjc3NzM1ZmUwMmYiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDY3OTkwNjEsImV4cCI6MTYwNjk3OTA2MX0.hOK_nvnMpNrScKBaVaUSKu7PqmpacfTXu0iknV01s-QPOpUN2b0IX-Zrm4RUSToM_oe2t_iUS9xFOMngajIYUA" ,"x-project-id":"537df655d1f34e22b318b97c9f4987b1"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFViIsImtleSI6IjNiN2NkMjUyMWUxODQ4ZTZhNzdjY2IxM2M5YzE0MGZlIiwidGVuYW50VHlwZSI6IkZMRVgiLCJkZWZhdWx0QWNjb3VudEFkbWluIjpmYWxzZSwidXNlckdyb3VwcyI6W10sImlzcyI6Imh0dHBzOi8vaW90ODMuY29tIiwiaWF0IjoxNjA2ODE0MTcyLCJleHAiOjE2MDY5OTQxNzJ9.kZR45MSeEsPrMmn8oFbTmZv9IrMJucOTeNiUi8U_cK4j7tlC3OLmz_uQfouptrCptT12lMMFi4XMOK6RM__Glg','x-project-id':'5dfa75dfcda34d94ac63fb5b1511f019'}
responseFromMigrant=requests.get("https://tracking.iot83.com/api/v2/gateway/api", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
print(dataFromMigrant[0])
count=0
for i in dataFromMigrant:
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
            payload["requestMethod"]=j["requestMethod"]
            payload["existingModule"]=True
            postCall = requests.post("https://track-penna.flex83.com/api/v4/gateway/api", json=payload,headers=headerForMigration, verify=False)
            count+=1
            print(count)
            print(postCall.json())
        except:
            print("error")

