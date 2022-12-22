from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import GroceryItem


def index(request):
    return HttpResponse("Hello World! You're at the grocery_list index.")