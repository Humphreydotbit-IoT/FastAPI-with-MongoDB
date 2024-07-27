from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://tunaungwai:Hsumonoo2@cluster0.wdytnji.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'),tlsAllowInvalidCertificates=True) #did not use certificate so allow withiut certificate
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.todo_db
collection_name = db["todo_collection"]

