import logging
from todo_project.db.config import get_database_client
from pymongo.errors import ConnectionFailure

logger = logging.getLogger(__name__)


def is_db_healthy():
    try:
        db_client = get_database_client()
        db_client.admin.command("ping")
        logger.info("Database connection established successfully")
        return True
    except ConnectionFailure as e:
        logger.error(f"Failed to establish database connection : {e}")
        return False
