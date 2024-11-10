from .base import *  # noqa: F403
import os

# Create the logs directory if it does not exists
os.makedirs("./logs", exist_ok=True)

DEBUG = False

ALLOWED_HOSTS = [".realdevsquad.com"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] [{levelname}] [{process} {thread}] [{module} {filename} {lineno}] - {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "level": DJANGO_LOG_LEVEL,  # noqa
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "./logs/todo.log",
            "formatter": "verbose",
            "level": DJANGO_LOG_LEVEL,  # noqa
            "when": "D",
            "interval": 1,
            "backupCount": 7,  # Retain only the last 7 days logs files
        },
    },
    "loggers": {
        "": {
            "level": DJANGO_LOG_LEVEL,  # noqa
            "handlers": ["console", "file"],
        },
        "django": {
            "level": DJANGO_LOG_LEVEL,  # noqa
            "handlers": ["console", "file"],
            "propagate": False,
        },
        "django.request": {
            "level": DJANGO_LOG_LEVEL,  # noqa
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}
