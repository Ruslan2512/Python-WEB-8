import pymongo
import json
from test_models import Author, Qoutes
from pymongo import MongoClient, InsertOne
import re

client = pymongo.MongoClient("mongodb+srv://ruslan:qwerty123@cluster.9diyzhg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection = db.author
requesting = []
lst = []

with open(r"authors.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

    result = collection.bulk_write(requesting)
    client.close()


