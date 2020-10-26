import pymongo
import urllib.parse
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["demosales_1584380202775"]
con=mydb["ETL_analytics_ODBBasicTracking_cc8a4220"]
point="Point"
location="location"
data=[]
data=list(con.aggregate([{"$geoNear":{"query":{location:{"type":point,"coordinates":[{"$toDouble":"$longitude"},{"$toDouble":"$latitude"}]}},"near": { "type": "Point", "coordinates": [ 72.8772618,21.4473103] } ,"maxDistance":100000,"distanceField":"test", "spherical": True}}]))
#data=list(con.find({"loc":{"$geoWithin":{"$centerSphere":[[80.2683422,26.4473103],10/6378.1]}}}))
print(data)
