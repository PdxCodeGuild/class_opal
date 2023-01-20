from django.shortcuts import render, HttpResponse
# from .models import User
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return HttpResponse("Index")


def Create(request):
    new_user = User.objects.create_user(...)
