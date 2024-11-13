from django.urls import path
from todo import views

urlpatterns = [
    path("health", views.HealthView.as_view(), name="health"),
]
