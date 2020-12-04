import requests,time
count=0

headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMGQyYjM2MmE5NGViNGJhYzgzMTRjZTBjMDMwOGEyZjkiLCJ0ZW5hbnRUeXBlIjoiRkxFWCIsImRlZmF1bHRBY2NvdW50QWRtaW4iOmZhbHNlLCJ1c2VyR3JvdXBzIjpbXSwiaXNzIjoiaHR0cHM6Ly9pb3Q4My5jb20iLCJpYXQiOjE2MDY5OTYxODIsImV4cCI6MTYwNzE3NjE4Mn0.sVPb5ZVKYY3Gf5iXxU8EMCVnCiD1i_eb5jb1aZQUvDVzmQ5-Mn7PNP-hYJRewHadyaxjZOe74gcPTtNDHRAq2A" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiZDk0MmVlMDlhNzMzNDE3YWE3MmQ5MjJlNTYxN2NlYjciLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDcwNTg4NDMsImV4cCI6MTYwNzIzODg0M30.DimJ83lcl7nr2i91Sv2NY5lJOkO98WKkfeeZbkvHIjYFGGivoXM66ijxnqEu-8kbFkcrnD859jaf3o4R1-cD7w','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
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

