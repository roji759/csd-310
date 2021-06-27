'''
Rogelio Orozco
CSD-310
Professor Sampson
6.25.21
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



print("-- DISPLAY STUDENTS DOCUMENTS FROM find() query --")


for doc in db.students.find():
 pprint(doc)

result = db.students.update_one({'_id': '1007'}, {'$set': {'last_name': 'Smith'}})


 
print("--DISPLAYING STUDENT DOCUMENT FROM find_one()--")

doc = db.students.find_one({'_id' : '1007'})

pprint(doc)