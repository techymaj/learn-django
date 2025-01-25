from django.http import HttpResponse, HttpResponseNotFound

from . import models


# Create your views here.

def monthly_challenge(request, month):
    for m in models.months:
        if m.casefold() == month.casefold():
            return HttpResponse(f"<h1>We are in {m}</h1>")
    else:
        return HttpResponseNotFound("Error:")
