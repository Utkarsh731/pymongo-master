import pymongo,time
import urllib.parse
start=time.time()
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["Tracking_1603959854482"]
con = mydb["ETL_analytics_ODBBasicTracking_537987b1"]
con_devices = mydb["deviceDetails_537987b1"]
con_vehicle =mydb["vehicleDetails_537987b1"]
current_time=int(time.time())*1000
con_vehicle.create_index()
data=[]
for i in con_devices.find():
    for j in con.find({"deviceId": i.get("id")}).sort("timestamp", -1).limit(1):
        if j.get("timestamp") > current_time - 900000:
            dic = {}
            dic["vehicleImage"] = None
            for k in con_vehicle.find({"deviceId": i.get("id")}):
                dic["vehicleImage"] = k.get("vehicleImage")

                dic["lat"] = float(j.get("latitude"))
                dic["lng"] = float(j.get("longitude"))
                dic["deviceId"] = i.get("id")
                dic["vehicleNum"] = i.get("vehicleNum")
                dic["simNum"] = i.get("simNum")
                startAdd = j.get("latitude") + ", " + j.get("longitude")
            #    dic["address"] = geolocatorStart.reverse(startAdd).address
                data.append(dic)
print(data)