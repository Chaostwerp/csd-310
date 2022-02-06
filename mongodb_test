#Module 5, assignment 5.2, William Fifield
#special thanks to my cat Magilou, for doubling as my rubber duck
import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttyt1.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

collections = db.list_collection_names()

print("-- Pytech Collection List --")
print (collections)

input ("\n\nEnd of program, press any key to exit...")
