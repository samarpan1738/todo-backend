from django.apps import AppConfig


class TodoConfig(AppConfig):
    name = "todo"

    def ready(self):
        from todo_project import checks  # noqa: F401
