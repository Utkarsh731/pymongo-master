import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["patient"]

mycol = mydb["patientDataset"]

mycol.insert_many([{"firstName":"Utkarsh","lastName":"Shukla","age":23,"history":{"disease":"soure throat","treatment":"Allegra120,Nice"}},
                   {"firstName":"Rahul","lastName":"Sharma","age":33,"history":{"disease":"cold","treatment":"Paracetalmol,Chestoncold"}},
                   {"firstName":"Kirt","lastName":"Shukla","age":44,"history":{"disease":"fever","treatment":"Dol500,Nice"}}])

mycol.update_one({"firstName":"Kirt"},{"$set":{"firstName":"Kirti","age":46,"history":{"disease":"viral fever","treatment":"Paracetamol,Nice"}}})

mycol.find({"age":{"$gt":30}})

mycol.delete_many({"history.disease":"cold"})

for i in mycol.find():print(i)