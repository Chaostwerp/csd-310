#pytech_insert
#Module 5, assignment 5.3, William Fifield
#special thanks to my cat Magilou, for doubling as my rubber duck
import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttyt1.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

students = db.students

jimothy = {
    "student_id": 1007,
    "first_name": "Jimothy",
    "last_name": "Mudlark"
}
jimothy_student_id = students.insert_one(jimothy).inserted_id

quonathan = {
    "student_id": 1008,
    "first_name": "Quonathan",
    "last_name": "Malarkey"
}
quonathan_student_id = students.insert_one(quonathan).inserted_id

roose_brillis = {
    "student_id": 1009,
    "first_name": "Roose",
    "last_name": "Brillis"
}
roose_brillis_student_id = students.insert_one(roose_brillis).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record Jimothy Mudlark into the students collection with document_id", jimothy_student_id)
print("Inserted student record Quonathan Malarkey into the students collection with document_id", quonathan_student_id)
print("Inserted student record Roose Brillis into the students collection with document_id", roose_brillis_student_id)

input ("\nEnd of program, press any key to exit...")
