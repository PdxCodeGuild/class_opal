from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BothUrls

def index(request):
    long_url = BothUrls.objects.

    return HttpResponse

def short_return(request):

    return HttpResponseRedirect