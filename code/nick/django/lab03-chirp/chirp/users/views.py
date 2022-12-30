from django.shortcuts import render, HttpResponse
from .models import User
# Create your views here.


def index(request):
    return HttpResponse("Index")


def Create(request):
    ...
