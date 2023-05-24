from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv('MONGODB_PASSWORD')
admin = os.getenv('MONGODB_ADMIN')
uri = f"mongodb+srv://{admin}:{password}@cluster0.miigi4x.mongodb.net/?retryWrites=true&w=majority"

db_client = MongoClient(uri,tlsCAFile=certifi.where(), server_api=ServerApi('1')).Cebrama
