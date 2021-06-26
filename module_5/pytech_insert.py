'''
Rogelio Orozco
CSD-310
Professor Sampson
6.24.21
'''

#import MongoClient
from pymongo import MongoClient

#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.b01mj.mongodb.net/pyTech?retryWrites=true&w=majority"

#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

#Create a variable named db and assign it to the pytech database instance.
db = client.pytech

col = db["students"]


#create first new entry
firstEntry =  {
    "_id": "1007", 
    "first_name" : "Rogelio", 
    "last_name" : "Orozco",
    "enrollments" : [
		{
			"term": "Spring 2021",
			"gpa": "3.7",
			"start_date": "2021-03-15",
			"end_date": "2021-07-25",
			#courses is an array of course_id values
			"courses": ["CSD-200", "CSD-205", "CSD-310", "CSD-320"]
		},
		{
			"term": "Fall 2021",
			"gpa": "3.7",
			"start_date": "2021-08-09",
			"end_date": "2021-12-19",
			"courses": ["CSD-340", "CSD-405", "CSD-360", "CSD-420"]
		},
    ]
}


x = col.insert_one(firstEntry).inserted_id
print("--  INSERT STATEMENTS --")
print("Inserted student record " + firstEntry["first_name"] + " " + firstEntry["last_name"] + " into the students collection " +
        "with student_id " + x)


#create second new entry
secEntry =  {
    "_id": "1008", 
    "first_name" : "Joe", 
    "last_name" : "Schmoe",
    "enrollments" : [
		{
			"term": "Spring 2021",
			"gpa": "2.9",
			"start_date": "2021-03-15",
			"end_date": "2021-07-25",
			#courses is an array of course_id values
			"courses": ["CSD-310", "CSD-320"]
		},
		{
			"term": "Fall 2021",
			"gpa": "3.1",
			"start_date": "2021-08-09",
			"end_date": "2021-12-19",
			"courses": ["CSD-340", "CSD-405"]
		},
    ]
}


y = col.insert_one(secEntry).inserted_id

print("Inserted student record " + secEntry["first_name"] + " " + secEntry["last_name"] + " into the students collection " +
        "with student_id " + y)

 #create third new entry
thirdEntry =  {
    "_id": "1009", 
    "first_name" : "Jane", 
    "last_name" : "Doe",
    "enrollments" : [
		{
			"term": "Spring 2021",
			"gpa": "3.8",
			"start_date": "2021-03-15",
			"end_date": "2021-07-25",
			#courses is an array of course_id values
			"courses": ["CSD-200", "CSD-320"]
		},
		{
			"term": "Fall 2021",
			"gpa": "3.7",
			"start_date": "2021-08-09",
			"end_date": "2021-12-19",
			"courses": ["CSD-405", "CSD-360"]
		},
    ]
}

z = col.insert_one(thirdEntry).inserted_id

print("Inserted student record " + thirdEntry["first_name"] + " " + thirdEntry["last_name"] + " into the students collection " +
        "with student_id " + z)

 