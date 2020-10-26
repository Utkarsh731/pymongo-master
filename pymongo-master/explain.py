import pymongo
import urllib.parse
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["demosales_1584380202775"]
mycol=mydb["ETL_analytics_ODBBasicTracking_cc8a4220"]
print(mycol.find({"deviceId":"170822567"}).limit(100000).explain()["executionStats"])