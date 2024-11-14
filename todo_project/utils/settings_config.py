import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_ENV_VAR_NAME = "DJANGO_ENV"
PRODUCTION = "PRODUCTION"
DEVELOPMENT = "DEVELOPMENT"
PRODUCTION_SETTINGS = "todo_project.settings.production"
DEVELOPMENT_SETTINGS = "todo_project.settings.development"
DEFAULT_SETTINGS = DEVELOPMENT_SETTINGS


def configure_settings_module():
    django_env = os.getenv(DJANGO_ENV_VAR_NAME, DEVELOPMENT).upper()

    django_settings_module = DEVELOPMENT_SETTINGS

    if django_env == PRODUCTION:
        django_settings_module = PRODUCTION_SETTINGS

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)
