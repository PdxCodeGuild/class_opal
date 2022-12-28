from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.


def index(request):
    incomplete_list = Item.objects.filter(
        completed=False, ).order_by('-creation_date')
    complete_list = Item.objects.filter(
        completed=True, ).order_by('-completed_date')
    context = {'incomplete_list': incomplete_list,
               'complete_list': complete_list}
    return render(request, 'grocery_list/index.html', context)


def delete(request):
    ...


def completer(request):
    ...
