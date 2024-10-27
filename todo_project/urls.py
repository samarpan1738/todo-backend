from django.urls import path
from todo_project.todo import views

urlpatterns = [
    path("health/", views.HealthView.as_view()),
]
