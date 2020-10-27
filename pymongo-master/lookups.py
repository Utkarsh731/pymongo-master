import pymongo,time
import urllib.parse
start=time.time()
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["demosales_1584380202775"]
con=mydb["deviceDetails_cc8a4220"]
duration=11
currentTime=int(time.time())*1000
beforeTime=currentTime-3600000*duration
data=list(con.aggregate([{"$lookup":{"from":"offlineDeviceHistory_cc8a4220","localField":"id","foreignField":"deviceId","as":"join"}},{"$unwind":"$join"},{"$match":{"join.status":"Offline","join.timestamp":{"$gte":beforeTime,"$lte":currentTime}}},{"$group":{"_id":"$vehicleNum","value":{"$sum":1}}},{"$project": {"_id":1,"value":1}}]))
print(time.time()-start)
print(data)
#{"join":{"$elemMatch":{"timestamp":{"$gte":beforeTime,"$lte":currentTime},"status":"Offline"}}}}