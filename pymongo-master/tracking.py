import uuid
import time

import pymongo
import urllib.parse
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["Tracking_1603959854482"]
con=mydb["customApiTrips_537987b1"]
argss = {
    "tripId": "",
    "tripStatus": "",
    "companyId": "xyz",
    "routeId": "xyz",
    "vehicleNo": "simulatedV1",
    "imeiNo": "xyz",
    "driverName": "xyz",
    "driverContact": "xyz",
    "invoiceNumber": "xyz",
    "netWeight": "xyz",
    "dO": "xyz",
    "invoiceDate": "xyz",
    "customerName": "xyz",
    "lrNo": "xyz",
    "Comments": "good",

}
commonJson = {
    "tripId": "",
    "tripStatus": "",
    "companyId": "",
    "routeId": "",
    "vehicleNo": "",
    "imeiNo": "",
    "driverName": "",
    "driverContact": "",
    "invoiceNumber": "",
    "netWeight": "",
    "dO": "",
    "invoiceDate": "",
    "customerName": "",
    "lrNo": "",
    "Comments": "",
    "createdAt": "",
    "updatedAt": ""

}
tripId = (uuid.uuid1()).hex
time_now = int(time.time() * 1000)

commonJson["tripId"] = tripId
commonJson["tripStatus"] = "active"
commonJson["companyId"] = argss.get("companyId")
commonJson["routeId"] = argss.get("routeId")
commonJson["vehicleNo"] = argss.get("vehicleNo")
commonJson["imeiNo"] = argss.get("imeiNo")
commonJson["driverName"] = argss.get("driverName")
commonJson["driverContact"] = argss.get("driverContact")
commonJson["createdAt"] = time_now
commonJson["updatedAt"] = time_now
response = con.insert_one(commonJson)
print(response)