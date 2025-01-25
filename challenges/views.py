from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import models


# Create your views here.


def index(request):
    li = []
    for month, _ in models.months.items():
        redirect_path = reverse("reversed-", args=[month])
        li.append(f"<li><a href={redirect_path}>{month}</a></li>")
    return HttpResponse(f"<ol>{"".join(li)}</ol>")


def monthly_challenge(request, month):
    for m, days in models.months.items():
        if m.casefold() == month.casefold():
            return HttpResponse(
                f"""
                    <h1>We are in {m}</h1>
                    <p>It has {days} days</p>
                """)
    else:
        return HttpResponseNotFound("Error:")
