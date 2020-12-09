import requests,time
count=0

headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjZiNmY3ZmJhNWMzNDYwOTg0OTJiYzkwYjZjZjRmMzIiLCJ0ZW5hbnRUeXBlIjoiRkxFWCIsImRlZmF1bHRBY2NvdW50QWRtaW4iOmZhbHNlLCJ1c2VyR3JvdXBzIjpbXSwiaXNzIjoiaHR0cHM6Ly9pb3Q4My5jb20iLCJpYXQiOjE2MDc0OTEzMzYsImV4cCI6MTYwNzY3MTMzNn0.jII-hqLkZnupXr2956cZeLMrSf6QZPVj1HxmsqYG3zD3j-4s0dYMGK_MxMo-z3co9ruiIJWXbO1K79rMJIfmBg" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjZiNmY3ZmJhNWMzNDYwOTg0OTJiYzkwYjZjZjRmMzIiLCJ0ZW5hbnRUeXBlIjoiRkxFWCIsImRlZmF1bHRBY2NvdW50QWRtaW4iOmZhbHNlLCJ1c2VyR3JvdXBzIjpbXSwiaXNzIjoiaHR0cHM6Ly9pb3Q4My5jb20iLCJpYXQiOjE2MDc0OTEzMzYsImV4cCI6MTYwNzY3MTMzNn0.jII-hqLkZnupXr2956cZeLMrSf6QZPVj1HxmsqYG3zD3j-4s0dYMGK_MxMo-z3co9ruiIJWXbO1K79rMJIfmBg','x-project-id':'5dfa75dfcda34d94ac63fb5b1511f019'}
responseFromMigrant=requests.get("https://track-penna.flex83.com/api/v4/actions", headers=headerForMigrant, verify=False)
codeFromMigrant=responseFromMigrant.json().get('data')
count=0
flexFaas=requests.get("https://track-penna.flex83.com/api/v4/actions",headers=headerForMigration,verify=False).json().get("data")
for i in codeFromMigrant:
    #print(i)
    responseCodeFromMigrant = requests.get("https://track-penna.flex83.com/api/v4/actions/" + i.get("id"),headers=headerForMigrant, verify=False)
    codeFromMigrant = responseCodeFromMigrant.json().get("data")
    code = codeFromMigrant.get("code").replace("pymongo.MongoClient(mongo_connect_url)","pymongo.MongoClient(mongo_connect_url,replicaSet='rs0')")
    imageName ="iot83/pymongo:v1_7d6eff69434d"
    overwrite = None
    requirements = []
    #codeMismatch=False
    createdAt=int(time.time())*1000
    createdBy="Utkarsh Shukla"
    createdByUserId="89d26617b44a4ae5830d18d8bac2e9c7"
    actionName = i.get("actionName")
    description = i.get("description")
    #gitCode=code
    imageDescription = i.get("imageDescription")
    kind = i.get("kind")
    #commitId=i.get("commitId")
    pathParameters = i.get("pathParameters")
    memory = int(128)
    description=""
    #wskActionName=i.get("actionName")+"_customWidgets"
    projectId="5dfa75dfcda34d94ac63fb5b1511f019"
    for k in flexFaas:
        if k.get("actionName")==actionName:
            id=k.get("id")
    responseFormat = {}
    payload = {"actionName": actionName,"createdBy":createdBy,
               "createdByUserId":createdByUserId,
               "createdAt":createdAt,"copyCount":0,"code": code,
               "description": description,
               "developmentMode": False, "imageDescription": imageDescription,
               "imageName": imageName, "kind": kind,"memory": memory, "pathParameters": pathParameters,
               "projectId":projectId,"raw":False,"timestamp":createdAt,
               "updatedAt":createdAt,"updatedBy":createdBy}
    try:
        postCall = requests.put("https://track-penna.flex83.com/api/v4/actions/"+id,
                                 json=payload, headers=headerForMigration, verify=False)
        print(postCall.text)
        count += 1
        print(count)
        print(actionName)
    except:
        print("error")
    break
