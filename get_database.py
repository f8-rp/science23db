import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://User:Password123@cluster0.ascretu.mongodb.net/?retryWrites=true&w=majority")
db = cluster["pollution"]
collection = db["data"]

object = {
   "location": "Santa Clara",
   "time": "3:40"
}

collection.insert_one(object)
