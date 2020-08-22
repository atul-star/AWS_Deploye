from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def test(req):
    return HttpResponse("<h1>Helllo</h1>")
