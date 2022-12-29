from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import datetime

from django.http import HttpResponseRedirect


from .models import GroceryItem



def index(request):
    latest_grocery_items = GroceryItem.objects.order_by('created_date')
    context = {
        'latest_grocery_items': latest_grocery_items,
    }

    return render(request, 'index.html', context)

def detail(request, text_desc_id):
    groceryitem = GroceryItem.objects.get(id=text_desc_id)
    print(groceryitem)
    return render(request, 'detail.html', {'groceryitem': groceryitem})

def add_item(request):
    GroceryItem.objects.create(text_desc=request.POST['input_item'])
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request):
    GroceryItem.objects.get(id=request.POST['delete_item']).delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete_item(request):
    item = GroceryItem.objects.get(text_desc=request.POST['complete_item'])
    item.is_complete = True
    item.completed_date = datetime.datetime.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def incomplete_item(request):
    item = GroceryItem.objects.get(text_desc=request.POST['incomplete_item'])
    item.is_complete = False
    item.completed_date = datetime.datetime.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))