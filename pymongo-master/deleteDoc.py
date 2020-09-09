import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["shop"] #shop=db name

mycol=mydb["product"] #product=collection name

query={'_id':ObjectId("5f57249b1c380c2ae186af9f")}

print(mycol.delete_one(query))

for i in mycol.find():print(i)