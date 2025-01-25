from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import models


# Create your views here.

def monthly_challenge(request, month, day):
    if day == 0:
        redirect_month = "december"
        redirect_day = 31
        redirect_path = reverse("reversed-", args=[redirect_month, redirect_day])
        print(f"Redirect path: {redirect_path}")
        return HttpResponseRedirect(redirect_path)
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
