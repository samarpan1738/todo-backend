from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo_project.todo import views

urlpatterns = [
    path('health/', views.HealthView.as_view()),
]