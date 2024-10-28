#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys

from dotenv import load_dotenv

load_dotenv()

DJANGO_ENV = "DJANGO_ENV"
PRODUCTION = "PRODUCTION"
DEVELOPMENT = "DEVELOPMENT"
PRODUCTION_SETTINGS = "todo_project.settings.production"
DEVELOPMENT_SETTINGS = "todo_project.settings.development"


def main():
    """Run administrative tasks."""
    django_env = os.getenv("DJANGO_ENV", DEVELOPMENT).upper()

    # Setting it to DEVELOPMENT
    django_settings_module = DEVELOPMENT_SETTINGS

    if django_env == PRODUCTION:
        django_settings_module = PRODUCTION_SETTINGS

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
