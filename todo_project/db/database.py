from django.conf import settings
from pymongo import MongoClient

mongo_client = None
db = None


def get_mongo_client():
    global mongo_client
    if mongo_client is None:
        mongo_client = _create_mongo_client()
    return mongo_client


def get_db():
    global db
    if db is None:
        db = get_mongo_client()[settings.DB_NAME]
    return db


def _create_mongo_client():
    return MongoClient(settings.MONGODB_URI)
