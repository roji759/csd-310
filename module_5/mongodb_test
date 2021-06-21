'''
Rogelio Orozco
CSD-310
Professor Sampson
6.20.21
'''

'''Import MongoClient
from pymongo import MongoClient
Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = “”;
Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)
Create a variable named db and assign it to the pytech database instance.
db = client.pytech
Using Python’s built-in print statement, calling the list_collection_names method off of the db variable.
print(db.list_collection_names)
Open a terminal window inside of VS Code.
Terminal > New Terminal
Under the “Problems” tab there will be a listing of any Python errors. Make sure you correct these before turning in your work.
Select the Terminal tab and run the program by selecting Run > Start Debugging
Continue to run and test the program until there are no errors and you can see the students collection in the terminal window.
'''

#import MongoClient
from pymongo import MongoClient

#Create a variable named url and assign it the connection string value you copied from MongoDB Atlas.
url = "mongodb+srv://admin:admin@cluster0.b01mj.mongodb.net/pyTech?retryWrites=true&w=majority"

#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

#Create a variable named db and assign it to the pytech database instance.
db = client.pytech

#Using Python’s built-in print statement, calling the list_collection_names method off of the db variable.
print("-- PyTech c0llection list --")
print(db.list_collection_names())
