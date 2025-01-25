from django.http import HttpResponse, HttpResponseNotFound

from . import models


# Create your views here.

def monthly_challenge(request, month, day):
    for m, days in models.months.items():
        if m.casefold() == month.casefold():
            return HttpResponse(
                f"""
                    <h1>We are in {m}</h1>
                    <p>It has {days} days</p>
                    <p>Your chosen date is <strong>{day}/{month}/2025</strong></p>
                """)
    else:
        return HttpResponseNotFound("Error:")
