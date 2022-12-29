from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem


def index(request):
    latest_grocery_item_list = GroceryItem.objects.order_by('-created_date')
    context = {'latest_grocery_item_list': latest_grocery_item_list}
    return render(request, 'grocery_list/index.html', context)


def add_item(request):
    GroceryItem.objects.create(description=request.POST['new_item'])
    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete_item(request):
    GroceryItem.objects.get(
        id=request.POST['delete_item']).delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def mark_complete(request):
    obj = GroceryItem.objects.get(description=request.POST['mark_complete'])
    obj.is_complete = True
    obj.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def mark_incomplete(request):
    obj = GroceryItem.objects.get(description=request.POST['mark_incomplete'])
    obj.is_complete = False
    obj.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
