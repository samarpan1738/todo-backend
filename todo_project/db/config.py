from django.conf import settings
from pymongo import MongoClient

database_client = None
db = None


def get_database_client():
    global database_client
    if database_client is None:
        database_client = MongoClient(settings.MONGODB_URI)
    return database_client


def get_database():
    global db
    if db is None:
        db = get_database_client()[settings.DB_NAME]
    return db
