from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.january),
    path("february", views.february),
]
