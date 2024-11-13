import logging
from django.conf import settings
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

logger = logging.getLogger(__name__)

database_client = None
db = None


def get_database_client():
    global database_client
    if database_client is None:
        database_client = MongoClient(
            settings.MONGODB_URI, serverSelectionTimeoutMS=5000, connectTimeoutMS=5000
        )
    return database_client


def get_database():
    global db
    if db is None:
        db = get_database_client()[settings.DB_NAME]
    return db


def is_healthy():
    try:
        db_client = get_database_client()
        db_client.admin.command("ping")
        logger.info("Database connection established successfully")
        return True
    except ConnectionFailure as e:
        logger.error(f"Failed to establish database connection : {e}")
        return False
