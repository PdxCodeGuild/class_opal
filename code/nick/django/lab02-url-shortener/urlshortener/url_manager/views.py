from django.shortcuts import render, HttpResponseRedirect, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world")
