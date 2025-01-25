from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from . import models


# Create your views here.

def monthly_challenge(request, month, day):
    if day == 0:
        return HttpResponseRedirect(f"/challenges/december/31")
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
