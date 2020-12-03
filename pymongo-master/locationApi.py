import requests
mobile="9873565969"
header={"authkey":"f8fabdfaa8014ddba8b702eb27440545"}
payload={"mobile":mobile}
response_location=requests.post("https://api.roado.co.in/rest/location/fetchLocation",json=payload,headers=header)
response_location=response_location.json()
if not response_location.get("success"):
    data_res=response_location["error"]["message"]
    code=400
    print(data_res)
print(response_location)
location_data=response_location.get("data").get("location")
print(location_data)