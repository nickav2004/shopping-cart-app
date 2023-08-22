from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Howdy<h1>")


def render_react(request):
    return render(request, "hello/index.html")


def greet(request, name):
    return HttpResponse(f"Howdy, {name.capitalize()}!")
