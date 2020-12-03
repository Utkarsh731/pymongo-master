import requests,time
count=0
headerForMigration={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiZjQxMjZkY2ZkMTI3NDM1NWI2OGU5MjZkNWI1YTUxZDEiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDM5Njg4NzksImV4cCI6MTYwNDE0ODg3OX0.KTsl7OVUMJJHjVg-wHpjR8xrx0MnutlDnvkLKjG0FtzFe7W9A1NB8igWL1IEE-oLlbbnZDl_8CMOljjl7dOOMw','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigration=requests.get("https://tracking.iot83.com/api/v2/actions/category?category=customWidgets", headers=headerForMigration, verify=False)
codeFromMigration=responseFromMigration.json().get("data")
for i in codeFromMigration:
    responseCodeFromMigrant = requests.get("https://tracking.iot83.com/api/v2/actions/" + i.get("id"),
                                           headers=headerForMigration, verify=False)
    codeFromMigrant = responseCodeFromMigrant.json().get("data")
    code = codeFromMigrant.get("code").replace("1929ebc5","537987b1")
    imageName = codeFromMigrant.get("imageName")
    overwrite = None
    requirements = []
    codeMismatch=False
    createdAt=int(time.time())*1000
    createdBy="Utkarsh Shukla"
    createdByUserId="89d26617b44a4ae5830d18d8bac2e9c7"
    actionName = i.get("actionName")
    description = i.get("description")
    gitCode=code
    imageDescription = i.get("imageDescription")
    kind = i.get("kind")
    commitId=i.get("commitId")
    pathParameters = i.get("pathParameters")
    memory = str(codeFromMigrant.get("memory"))
    description=""
    wskActionName=i.get("actionName")+"_customWidgets"
    projectId="537df655d1f34e22b318b97c9f4987b1"
    id=i.get("id")
    responseFormat = {}
    payload = {"actionName": actionName,"gitCode":code,"createdBy":createdBy,"createdByUserId":createdByUserId,"description":description ,"createdAt":createdAt,"copyCount":0,"commitId":commitId,"codeMismatch":codeMismatch,"category": "customWidgets", "code": code, "description": description,
               "developmentMode": False, "imageDescription": imageDescription, "imageName": imageName, "kind": kind,"wskActionName":wskActionName,
               "memory": memory, "overwrite": overwrite, "pathParameters": pathParameters, "requirements": requirements,
               "responseFormat": responseFormat, "saveAsDraft": False,"projectId":projectId,"raw":False,"timestamp":createdAt,"updatedAt":createdAt,"updatedBy":createdBy,"verifiedUser":True,"wskActionNamewskActionName":wskActionName}
    try:
        postCall = requests.put("https://tracking.iot83.com/api/v2/actions/"+id+"?pushToGit=true&commitMessage=test",
                                 json=payload, headers=headerForMigration, verify=False)
        print(postCall.text)
        count += 1
        print(count)
        print(actionName)
    except:
        print("error")