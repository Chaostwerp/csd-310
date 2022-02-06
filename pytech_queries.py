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

student = db.students.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one QUERY --")

print("Student ID: ",student["student_id"],
"\nFirst Name: ", student["first_name"],
"\nLast Name: ", student["last_name"], "\n")

input ("\nEnd of program, press any key to exit...")