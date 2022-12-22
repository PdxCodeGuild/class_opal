from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from .models import GroceryItem


def index(request):
    incomplete_items = GroceryItem.objects.filter(
        completed=False).order_by('date_created')
    completed_items = GroceryItem.objects.filter(
        completed=True).order_by('date_completed')
    # context is what it's called in database
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    # render puts stuff in db
    return render(request, 'grocery_list/index.html', context)

def add(request):
    new_item = GroceryItem.objects.create(item_description=request.POST['item_description'])
    return HttpResponseRedirect(reverse('grocery_list:index', args=(new_item.id,))) #reverse means django figures out URL for me
