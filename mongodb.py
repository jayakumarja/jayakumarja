from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client.jay
j=db.user
#a=db.info
