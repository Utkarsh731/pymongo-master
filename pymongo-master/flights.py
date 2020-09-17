import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["flights"] #shop=db name

mycol=mydb["flightData"] #product=collection name

for i in mycol.find():print(i)