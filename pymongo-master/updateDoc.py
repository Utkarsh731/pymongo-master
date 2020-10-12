import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["flights"]  # shop=db name

mycol = mydb["passengers"]  # product=collection name

mycol.update_many({},{"$set":{"hobbies":["cricket","football"]}})

print(mycol.find_one({"name": "Albert Twostone"})["hobbies"])