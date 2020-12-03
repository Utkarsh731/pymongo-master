import pymongo
import urllib.parse
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["demosales_1584380202775"]
con=mydb["ETL_analytics_geoQueriesData_cc8a4220"]
point="Point"
location="loc"
data=[]
#data=list(con.aggregate([{"$geoNear":{"query":{location:{"type":point,"coordinates":[{"$toDouble":"$longitude"},{"$toDouble":"$latitude"}]}},"near": { "type": "Point", "coordinates": [ 72.8772618,21.4473103] } ,"maxDistance":100000,"distanceField":"test", "spherical": True}}]))
data=list(con.find({"loc":{"$geoWithin":{"$centerSphere":[[80.2683422,26.4473103],100/6378.1]}}}))
print(data)
97Z stdout: score========0
2020-10-29T08:54:32.451609875Z stdout: getHa===20
2020-10-29T08:54:32.451632467Z stdout: getHb===10
2020-10-29T08:54:32.451635391Z stdout: getHc===20
2020-10-29T08:54:32.451637646Z stdout: getOs===30
2020-10-29T08:54:32.451639958Z stdout: getId===20
2020-10-29T08:54:32.451642154Z stdout: distance===400.0
2020-10-29T08:54:32.451644434Z stdout: Ha===0
2020-10-29T08:54:32.451648842Z stdout: Hc===0
2020-10-29T08:54:32.451650942Z stdout: osd===0
2020-10-29T08:54:32.451653054Z stdout: idleTIme===695
2020-10-29T08:54:32.451655176Z stdout: runningTIme===41
2020-10-29T08:54:32.451657404Z stdout: ==============================================
2020-10-29T08:54:32.451659699Z stdout: score========-239.02439024390247