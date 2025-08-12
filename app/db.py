from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["slack_bot"]

def save_message(message):
    db.messages.insert_one({"text": message})