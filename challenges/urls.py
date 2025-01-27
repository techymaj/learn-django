from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="challenge"),
    path(
        "<str:month>",
        views.monthly_challenge,
        name="reversed-"
    ),
]
