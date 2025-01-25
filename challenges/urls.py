from django.urls import path
from . import views

urlpatterns = [
    path(
        "<str:month>/<int:day>",
        views.monthly_challenge,
        name="reversed-"
    ),
]
