#pytech_queries
#Module 5, assignment 5.3, William Fifield
#special thanks to my cat Magilou, for doubling as my rubber duck

import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ttyt1.mongodb.net/pytech"

client = MongoClient(url)

db = client.pytech

students = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    print("Student ID: ",student["student_id"],
    "\nFirst Name: ", student["first_name"],
    "\nLast Name: ", student["last_name"], "\n")



alouiscious = {
    "student_id": 1010,
    "first_name": "Alouiscious",
    "last_name": "Hooligan"
}
alouiscious_student_id = db.students.insert_one(alouiscious).inserted_id

short_term = db.students.find_one({"student_id": 1010})

print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document-id ", short_term["_id"])

print("\n-- DISPLAYING STUDENT TEST DOC --")

print("Student ID: ", short_term["student_id"],
    "\nFirst Name: ", short_term["first_name"],
    "\nLast Name: ", short_term["last_name"], "\n")

db.students.delete_one({"student_id": 1010})


students = db.students.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    print("Student ID: ",student["student_id"],
    "\nFirst Name: ", student["first_name"],
    "\nLast Name: ", student["last_name"], "\n")


input("\nEnd of program, press any key to exit...")