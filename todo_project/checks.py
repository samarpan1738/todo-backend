from django.core.checks import Error, register, Tags

from todo_project.db.database import get_mongo_client
from pymongo.errors import ConnectionFailure
import logging

logger = logging.getLogger(__name__)


@register(Tags.database)
def mongo_connection_check(app_configs, **kwargs):
    mongo_client = get_mongo_client()
    errors = []
    try:
        mongo_client.admin.command("ping")
        logger.info("MongoDB connection established successfully")
    except ConnectionFailure as e:
        logger.error(f"MongoDB connection failed: {e}")
        errors.append(Error("Failed to establish MongoDB connection"))
    return errors
