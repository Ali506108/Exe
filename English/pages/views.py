from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def exe(requests):
    return HttpResponse("<h1>Hi bro</h1>")
