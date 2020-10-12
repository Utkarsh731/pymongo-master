import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["flights"] #shop=db name

mycol=mydb["flightData"] #product=collection name
dataSet= list(mycol.find())#list will convert the cursor into list of dic
print(dataSet)
