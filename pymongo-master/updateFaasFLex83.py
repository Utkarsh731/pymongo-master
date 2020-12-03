import requests,time
count=0

headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFViIsImtleSI6IjNiN2NkMjUyMWUxODQ4ZTZhNzdjY2IxM2M5YzE0MGZlIiwidGVuYW50VHlwZSI6IkZMRVgiLCJkZWZhdWx0QWNjb3VudEFkbWluIjpmYWxzZSwidXNlckdyb3VwcyI6W10sImlzcyI6Imh0dHBzOi8vaW90ODMuY29tIiwiaWF0IjoxNjA2ODE0MTcyLCJleHAiOjE2MDY5OTQxNzJ9.kZR45MSeEsPrMmn8oFbTmZv9IrMJucOTeNiUi8U_cK4j7tlC3OLmz_uQfouptrCptT12lMMFi4XMOK6RM__Glg" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiYjAzZjQ3M2U1ZjUwNDhhN2JmMTlmMDA0YWY1OTkwMjEiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDY5NzUwMTUsImV4cCI6MTYwNzE1NTAxNX0.bzhMQQsyd3lg4kxBC8a6ljCbIwYXwj80dtVWjP9XaFP4RsvR5HoDbkfePHA7u4UIxVxSHyU83yJqeuvMwSS10Q','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://tracking.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigrant, verify=False)
codeFromMigrant=responseFromMigrant.json().get('data')
count=0
flexFaas=requests.get("https://track-penna.flex83.com/api/v4/actions",headers=headerForMigration,verify=False).json().get("data")
for i in codeFromMigrant:
    #print(i)
    responseCodeFromMigrant = requests.get("https://tracking.iot83.com/api/v2/actions/" + i.get("id"),headers=headerForMigrant, verify=False)
    codeFromMigrant = responseCodeFromMigrant.json().get("data")
    code = codeFromMigrant.get("code").replace("537987b1","5df1f019")
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
