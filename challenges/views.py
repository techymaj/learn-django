from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from . import models


# Create your views here.

def base(request):
    return render(request, "challenges/index.html", {
        "name": "majaliwa m. Wilfried",
        "arr": [5, 4, 3, 2, 1]
    })


def index(request):
    challenges = {}
    for month, _ in models.months.items():
        # challenge/month
        redirect_path = reverse("reversed-", args=[month])
        challenges.update({month: redirect_path})
    return render(request, "challenges/challenges.html", {
        "challenges": challenges,
    })


def monthly_challenge(request, month):
    for m, days in models.months.items():
        if m.casefold() == month.casefold():
            return HttpResponse(
                f"""
                    <h1>We are in {m}</h1>
                    <p>It has {days} days</p>
                """)
    else:
        raise Http404("404.html")
