import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["companyData"]
mycol=mydb["companies"]
mycol.insert_one({"name":"83incs","stock":100,"_id":1})
mycol.insert_many([{"name":"iot83","stock":110,"_id":2},{"name":"83apps","stock":1010,"_id":3}])
mycol.insert_many([{"name":"iot83","stock":110,"_id":2},{"name":"apps83","stock":1010,"_id":4}],ordered=False)
mycol.insert_one({"name":"arrow","_id":5},pymongo.WriteConcern(w=1,j=True))

for i in mycol.find():print(i)