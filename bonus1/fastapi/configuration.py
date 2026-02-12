
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://db_user:LwUHIGWNqF5jQtrR@witty-coder-1.iy8p1eb.mongodb.net/?appName=witty-coder-1"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]