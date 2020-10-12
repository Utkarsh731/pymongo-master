import pymongo
from collections import OrderedDict
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["twets"]
query = [(),
        ('validator', {'phone': {'$type': 'string'}}),
        ('validationLevel', 'moderate')]
query = OrderedDict(query)
db.command(query)

