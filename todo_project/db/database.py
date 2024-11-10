from django.conf import settings
from pymongo import MongoClient

mongo_client = None
db = None


def get_mongo_client():
    global mongo_client
    if mongo_client is None:
        mongo_client = MongoClient(settings.MONGODB_URI)
    return mongo_client


def get_db():
    global db
    if db is None:
        db = get_mongo_client()[settings.DB_NAME]
    return db
