import pymongo
import urllib.parse
username = urllib.parse.quote_plus('m83app_read')
password = urllib.parse.quote_plus('qwerty@123')
myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
mydb = myclient["BMCSoftware_1602478609616"]
mycol=mydb["ETL_analytics_ODBBasicTracking_dc3fee8b"]
print(mycol.find({"deviceId":"170822567"}).limit(1000).explain()["executionStats"])