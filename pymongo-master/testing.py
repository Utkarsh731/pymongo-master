import datetime as dt
response={
    "count": 0,
    "end": True,
    "page": 1,
    "success": False
}
data,dataSet=[],[]
success = True
if not response.get("success"):
    success = False
    print("")
if success:
    print("suc")
for i in dataSet:
    dic = {"carrier": None, "lat": None, "lng": None, "timestamp": None, "driverPhoneNo": None, "registrationNo": None,
           "address": None}
    dic["carrier"] = i.get("carrier")
    if i.get("location").get("latitude"):
        dic["lat"] = i["location"]["latitude"]
        dic["lng"] = i["location"]["longitude"]
        dic["address"] = i["location"]["address"]
        time = i["location"]["timestamp"]
        date_time_obj = dt.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
        time = int(date_time_obj.timestamp() * 1000 + 5.5 * 3600000)
        dic["timestamp"] = time
    dic["driverPhoneNo"] = i["mobile"]
    dic["registrationNo"] = i["vehicleNo"]
    dic["driver"] = i["name"]
    data.append(dic)
print(data
)