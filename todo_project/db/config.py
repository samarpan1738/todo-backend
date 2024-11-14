from django.conf import settings
from pymongo import MongoClient
from todo_project.constants.database import SERVER_SELECTION_TIMEOUT_MS, CONNECT_TIMEOUT_MS

database_client = None
db = None


def get_database_client():
    global database_client
    if database_client is None:
        database_client = MongoClient(
            settings.MONGODB_URI,
            serverSelectionTimeoutMS=SERVER_SELECTION_TIMEOUT_MS,
            connectTimeoutMS=CONNECT_TIMEOUT_MS,
        )
    return database_client


def get_database():
    global db
    if db is None:
        db = get_database_client()[settings.DB_NAME]
    return db
