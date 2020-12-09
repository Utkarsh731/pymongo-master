import requests,time
count=0

headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjZiNmY3ZmJhNWMzNDYwOTg0OTJiYzkwYjZjZjRmMzIiLCJ0ZW5hbnRUeXBlIjoiRkxFWCIsImRlZmF1bHRBY2NvdW50QWRtaW4iOmZhbHNlLCJ1c2VyR3JvdXBzIjpbXSwiaXNzIjoiaHR0cHM6Ly9pb3Q4My5jb20iLCJpYXQiOjE2MDc0OTEzMzYsImV4cCI6MTYwNzY3MTMzNn0.jII-hqLkZnupXr2956cZeLMrSf6QZPVj1HxmsqYG3zD3j-4s0dYMGK_MxMo-z3co9ruiIJWXbO1K79rMJIfmBg" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiZTgxMWViZWMzZmNjNGZhZWIwMTQ2ODkyNDEwODFlMTciLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDc1MTI5NTEsImV4cCI6MTYwNzY5Mjk1MX0.6cYVBqJG22BYiO3PXUSp8Nlrjs8AUJ3wjX5YgbMKzE7On6yWC1-qRBLqPNN_6EvCBCFtf_lf17aSRI7nb8JNMA','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://tracking.iot83.com/api/v2/widgets?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
count=0
currentTime=int(time.time())*1000
flexFaas=requests.get("https://track-penna.flex83.com/api/v4/pages",headers=headerForMigration,verify=False).json().get("data")
for i in dataFromMigrant:
    responseCodeFromMigrant = requests.get("https://tracking.iot83.com/api/v2/widgets/" + i.get("id"),headers=headerForMigrant, verify=False)
    codeFromMigrant = responseCodeFromMigrant.json().get("data")
    print(codeFromMigrant)
    projectId="5dfa75dfcda34d94ac63fb5b1511f019"
    for k in flexFaas:
        if k.get("name")==i["widgetName"]:
            print("name found")
            id=k.get("id")
    code=codeFromMigrant["data"]
    createdAt=currentTime
    createdBy="Utkarsh Shukla"
    createdByUserId="0ab561cfff2f415db3a672f824f73b8a"
    description=""
    name=codeFromMigrant["widgetName"]
    settings=codeFromMigrant["widgetSettings"]
    updatedAt=currentTime
    updatedBy="Utkarsh Shukla"
    payload = {"code": code,"createdAt":createdAt,"createdBy":createdBy,
               "createdByUserId":createdByUserId,
               "description": description,"id":id,"name": name,
               "projectId":projectId,"settings":settings,
               "updatedAt":createdAt,"updatedBy":createdBy}
    try:
        postCall = requests.put("https://track-penna.flex83.com/api/v4/pages/"+id,
                                 json=payload, headers=headerForMigration, verify=False)
        print(postCall.text)
        count += 1
        print(count)
        print(name)
    except:
        print(postCall.json())
        print("error")

