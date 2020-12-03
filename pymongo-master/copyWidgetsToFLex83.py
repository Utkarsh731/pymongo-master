import requests,json
headerForMigration = { 'X-Authorization' : 'Bearer ' + "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiMGFiNTYxY2ZmZjJmNDE1ZGIzYTY3MmY4MjRmNzNiOGEiLCJ0ZW5hbnQiOiJ0cmFjay1wZW5uYSIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJCQUNLRU5EX0RFViIsImtleSI6IjNiN2NkMjUyMWUxODQ4ZTZhNzdjY2IxM2M5YzE0MGZlIiwidGVuYW50VHlwZSI6IkZMRVgiLCJkZWZhdWx0QWNjb3VudEFkbWluIjpmYWxzZSwidXNlckdyb3VwcyI6W10sImlzcyI6Imh0dHBzOi8vaW90ODMuY29tIiwiaWF0IjoxNjA2ODE0MTcyLCJleHAiOjE2MDY5OTQxNzJ9.kZR45MSeEsPrMmn8oFbTmZv9IrMJucOTeNiUi8U_cK4j7tlC3OLmz_uQfouptrCptT12lMMFi4XMOK6RM__Glg" ,"x-project-id":"5dfa75dfcda34d94ac63fb5b1511f019"}
headerForMigrant={'X-Authorization':'Bearer '+'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1dGthcnNoLnNodWtsYUA4M2luY3MuY29tIiwianRpIjoiODlkMjY2MTdiNDRhNGFlNTgzMGQxOGQ4YmFjMmU5YzciLCJ0ZW5hbnQiOiJ0cmFja2luZyIsIm5hbWUiOiJVdGthcnNoIFNodWtsYSIsImlzVmVyaWZpZWQiOnRydWUsImlzTGljZW5zZUV4cGlyZWQiOmZhbHNlLCJpbnRlcm5hbFVzZXIiOnRydWUsInJvbGUiOiJNVUxUSV9ST0xFIiwia2V5IjoiYjAzZjQ3M2U1ZjUwNDhhN2JmMTlmMDA0YWY1OTkwMjEiLCJpc3MiOiIyMTRhYTNkZS0xOWMwLTExZWItYTNjNC0wMmY1Nzg3NjRiZmEiLCJpYXQiOjE2MDY5NzUwMTUsImV4cCI6MTYwNzE1NTAxNX0.bzhMQQsyd3lg4kxBC8a6ljCbIwYXwj80dtVWjP9XaFP4RsvR5HoDbkfePHA7u4UIxVxSHyU83yJqeuvMwSS10Q','x-project-id':'537df655d1f34e22b318b97c9f4987b1'}
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
