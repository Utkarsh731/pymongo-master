import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["shop"] #shop=db name

mycol=mydb["product"] #product=collection name

print(myclient.list_database_names())

print(mydb.list_collection_names())

print(mycol.find_one())
