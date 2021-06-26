'''
Rogelio Orozco
CSD-310
Professor Sampson
6.25.21
'''

#import MongoClient
from pymongo import MongoClient

#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.b01mj.mongodb.net/pyTech?retryWrites=true&w=majority"

#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

#Create a variable named db and assign it to the pytech database instance.
db = client.pytech


docs = db.students
print("-- DISPLAY STUDENTS DOCUMENTS FROM find() query --")

for doc in docs.find():
 print(doc)

doc = db.students.find_one({"_id" : "1007"})
 
print("DISPLAYING STUDENT DOCUMENT FROM find_one()")

print(doc)