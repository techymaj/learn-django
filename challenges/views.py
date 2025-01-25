from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def january(request):
    return HttpResponse("<h1>Hello There!</h1>")


def february(request):
    return HttpResponse("It's not yet february")
