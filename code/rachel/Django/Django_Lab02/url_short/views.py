from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BothUrls
from .forms import URLForm
import random

def index(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            options = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            code = [random.choice(options) for i in range(6)]
        return HttpResponse()

def short_return(request):

    return HttpResponseRedirect