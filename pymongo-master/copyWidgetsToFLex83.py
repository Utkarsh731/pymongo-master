import requests,json
headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJBQ0NPVU5UX0FETUlOIiwia2V5IjoiMjZiNmY3ZmJhNWMzNDYwOTg0OTJiYzkwYjZjZjRmMzIiLCJ0ZW5hbnRUeXBlIjoiRkxFWCIsImRlZmF1bHRBY2NvdW50QWRtaW4iOmZhbHNlLCJ1c2VyR3JvdXBzIjpbXSwiaXNzIjoiaHR0cHM6Ly9pb3Q4My5jb20iLCJpYXQiOjE2MDc0OTEzMzYsImV4cCI6MTYwNzY3MTMzNn0.jII-hqLkZnupXr2956cZeLMrSf6QZPVj1HxmsqYG3zD3j-4s0dYMGK_MxMo-z3co9ruiIJWXbO1K79rMJIfmBg" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiZTgxMWViZWMzZmNjNGZhZWIwMTQ2ODkyNDEwODFlMTciLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDc1MTI5NTEsImV4cCI6MTYwNzY5Mjk1MX0.6cYVBqJG22BYiO3PXUSp8Nlrjs8AUJ3wjX5YgbMKzE7On6yWC1-qRBLqPNN_6EvCBCFtf_lf17aSRI7nb8JNMA','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
responseFromMigrant=requests.get("https://tracking.iot83.com/api/v2/widgets?category=customWidgets", headers=headerForMigrant, verify=False)
dataFromMigrant=responseFromMigrant.json().get('data')
print(dataFromMigrant[0])
count=0
for i in dataFromMigrant:
    responseCodeFromMigrant=requests.get("https://tracking.iot83.com/api/v2/widgets/"+i["id"], headers=headerForMigrant, verify=False).json().get('data')
    code=responseCodeFromMigrant.get("data")
    description = responseCodeFromMigrant.get("description")
    name = responseCodeFromMigrant.get("widgetName")
    settings=responseCodeFromMigrant.get("widgetSettings")
    payload={"code":code,"description":description,"name":name,"settings":settings}
    try:
        postCall = requests.post("https://track-penna.flex83.com/api/v4/pages", json=payload,headers=headerForMigration, verify=False)
        count += 1
        print(count)
    except:
        print("error")
