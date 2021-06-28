'''
Rogelio Orozco
CSD-310
Professor Sampson
6.27.21
'''
#import MongoClient
from pymongo import MongoClient
from pprint import pprint

#Create a variable named url and assign it the MongoDB Atlas connection string.
url = "mongodb+srv://admin:admin@cluster0.b01mj.mongodb.net/pyTech?retryWrites=true&w=majority"

#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

#Create a variable named db and assign it to the pytech database instance.
db = client.pytech


#Call the find() method and display the results to the terminal window
print("--DISPLAYING STUDENT DOCUMENT FROM find() query--")
for doc in db.students.find({},{ "first_name" : 1, "last_name" : 1}):
    pprint(doc)

#Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
result = db.students.insert_one({
    "_id": "1010", 
    "first_name" : "Severus", 
    "last_name" : "Snape",
    "enrollments" : [
		{
			"term": "Spring 2022",
			"gpa": "4.0",
			"start_date": "2022-03-15",
			"end_date": "2022-07-25",
			"courses": ["CSD-200", "CSD-205", "CSD-310", "CSD-320"]
		},
		{
			"term": "Fall 2022",
			"gpa": "3.9",
			"start_date": "2022-08-09",
			"end_date": "2022-12-19",
			"courses": ["CSD-340", "CSD-405", "CSD-360", "CSD-420"]
		},
    ]
})

print("--  INSERT STATEMENTS --")
print("Inserted student record into the students collection with document id: " + result.inserted_id)

#Call the find_one() method and display the results to the terminal window.
print("--DISPLAYING STUDENT TEST DOC--")
pprint(db.students.find_one({"_id" : "1010"}, { "first_name" : 1, "last_name" : 1}))


#Call the delete_one() method by student_id 1010.
result = db.students.delete_one({"_id" : "1010"})

#Call the find() method and display the results to the terminal window
print("--DISPLAYING STUDENT DOCUMENT FROM find() query--")
for doc in db.students.find({},{ "first_name" : 1, "last_name" : 1}):
    pprint(doc)
