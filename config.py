from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://admin:adminpass@localhost:27017/surveyDB?authSource=admin')

def get_database():
    client = MongoClient(MONGO_URI)
    return client.surveyDB