import pymongo,time
import urllib.parse
start=time.time()
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["Tracking_1603959854482"]
con_data=mydb["ETL_analytics_ODBBasicTracking_537987b1"]
con_history=mydb["offlineDeviceHistory_537987b1"]
con_devices=mydb["deviceDetails_537987b1"]
con_veh=mydb["vehicleDetails_537987b1"]
devices = con_devices.distinct("id")
current_time = int(time.time()) * 1000
duration = 1
lastStatus, flag = "Offline", False
if not duration:
    duration = 24
else:
    duration = int(duration)
before_time = current_time - 3600000 * duration

data = []
for i in con_devices.find():
    for j in con_data.find({"deviceId": i.get("id")}).sort("timestamp", -1).limit(1):
        if i.get("vehicleNum")=="KA01AB7509":
            print(j)
        if j.get("timestamp") > (current_time - 900000):
            print("device is online")
            for img in con_veh.find({"deviceId": i.get("id")}):
                vehicleImage = img.get("vehicleImage")
            dic = {}
            dic["vehicleImage"] = vehicleImage
            gsm = int(j.get("GSMSignal"))
            dic["deviceId"] = i.get("id")
            dic["vehicleNum"] = i.get("vehicleNum")
            dic["GSMSignal"] = gsm
            if gsm <= 0:
                dic["GSMCategory"] = "low"
            elif gsm == 1:
                dic["GSMCategory"] = "Poor"
            elif gsm >= 2 and gsm <= 30:
                dic["GSMCategory"] = "Average"
            elif gsm >= 31:
                dic["GSMCategory"] = "Good"
            dic["lowBatteryStatus"] = j.get("lowBatteryStatus")
            historyRecord = {}
            history = []
            for k in con_history.find(
                    {"deviceId": i.get("id"), "timestamp": {"$gte": before_time, "$lte": current_time}},
                    {"_id": 0}).sort("timestamp", 1):
                if k.get("status") == lastStatus:
                    flag = True
                    historyRecord = {"startTimestamp": k.get("timestamp"), "startLatitude": float(k.get("latitude")),
                                     "startLongitude": float(k.get("longitude")), "reason": k.get("reason")}
                elif flag and k.get("status") != lastStatus:
                    lastStatus = k.get("status")
                    historyRecord["endTimestamp"] = k.get("timestamp")
                    historyRecord["endLatitude"] = float(k.get("latitude"))
                    historyRecord["endLongitude"] = float(k.get("longitude"))
                    history.append(historyRecord)
            dic["offlineHistory"] = history
            data.append(dic)
print(data)