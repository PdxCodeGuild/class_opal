from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime
from . models import GroceryItem


def index(request):
    if request.method == 'POST':
        form_data = request.POST
        grocery_object = GroceryItem.objects.create(
            text_description=form_data['text_description'], 
            created_date=datetime.now(), 
            completed_date=datetime.now(), 
            completed=False
        )
        return HttpResponseRedirect(reverse('grocery_list:index'))

    else:
        grocery_list = GroceryItem.objects.all()
        context = {'grocery_list': grocery_list}
        return render(request, 'grocery_list/index.html', context)

def complete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    if grocery_item.completed == False:
        grocery_item.completed = True
    else:
        grocery_item.completed = False
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, id):
    grocery_item = GroceryItem.objects.get(id=id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))