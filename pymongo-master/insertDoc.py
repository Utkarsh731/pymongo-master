import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["shop"]  # shop=db name

mycol = mydb["product"]  # product=collection name

# mycol.insert_one({"name":"A Pen","price":2})

for i in mycol.find(): print(i)
print(myclient.database_names())
