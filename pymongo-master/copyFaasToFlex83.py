import requests
headerForMigrant = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiNWYyNDk1NDdkYjM4NGUxNDlkN2UwYjc3NzM1ZmUwMmYiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDY3OTkwNjEsImV4cCI6MTYwNjk3OTA2MX0.hOK_nvnMpNrScKBaVaUSKu7PqmpacfTXu0iknV01s-QPOpUN2b0IX-Zrm4RUSToM_oe2t_iUS9xFOMngajIYUA" ,"x-project-id":"537df655d1f34e22b318b97c9f4987b1"}
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFViIsImtleSI6IjNiN2NkMjUyMWUxODQ4ZTZhNzdjY2IxM2M5YzE0MGZlIiwidGVuYW50VHlwZSI6IkZMRVgiLCJkZWZhdWx0QWNjb3VudEFkbWluIjpmYWxzZSwidXNlckdyb3VwcyI6W10sImlzcyI6Imh0dHBzOi8vaW90ODMuY29tIiwiaWF0IjoxNjA2ODE0MTcyLCJleHAiOjE2MDY5OTQxNzJ9.kZR45MSeEsPrMmn8oFbTmZv9IrMJucOTeNiUi8U_cK4j7tlC3OLmz_uQfouptrCptT12lMMFi4XMOK6RM__Glg','x-project-id':'5dfa75dfcda34d94ac63fb5b1511f019'}
responseFromMigrant=requests.get("https://tracking.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=0
#faasOnFLex=requests.get("https://track-penna.flex83.com/api/v4/actions",headers=headerForMigration,verify=False).json().get("data")
#actionsOnFlex=[]
#for i in faasOnFLex:
#    actionsOnFlex.append(i["actionName"])
#actionsNotIncluded=[]
#for i in dataFromMigrant:
#    if i.get("actionName") not in actionsOnFlex:
#        actionsNotIncluded.append(i.get("actionName"))
#print(actionsNotIncluded)
for dataSet in dataFromMigrant:
    codeSet = responseCodeFromMigrant = requests.get("https://tracking.iot83.com/api/v2/actions/" + dataSet.get("id"),
                                                     headers=headerForMigrant, verify=False).json().get("data")
    params = {"actionName": dataSet["actionName"],
              "code": codeSet["code"],
              "description": dataSet["description"],
              "developmentMode": False,
              "imageDescription": dataSet["imageDescription"],
              "imageName": "iot83/pymongo:v1_7d6eff69434d",
              "kind": dataSet["kind"],
              "memory": "256",
              "pathParameters": dataSet["pathParameters"],
              "raw": False}
    try:
        postRequest = requests.post("https://track-penna.flex83.com/api/v4/actions", headers=headerForMigration,
                                    verify=False, json=params).json()
        count += 1
    except:
        print(postRequest)
    print(postRequest)
    print(count)


