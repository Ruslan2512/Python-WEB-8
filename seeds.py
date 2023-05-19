import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb+srv://ruslan:qwerty123@cluster.9diyzhg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection = db.author
requesting = []

with open("authors.json", "r") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()