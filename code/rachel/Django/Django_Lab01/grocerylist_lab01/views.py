from django.shortcuts import render, get_object_or_404
# * 4 x views 
#     * bring up index page that lists to-dos
#     * create new grocery list
#     * marking complete / incomplete (if completed = true ...)
#     * deleting item
from django.http import HttpResponseRedirect
from .models import GroceryItem
from django.urls import reverse
from django.utils import timezone

def index(request):
    completed_items = GroceryItem.objects.filter(completed_y_n=True)
    incomplete_items = GroceryItem.objects.filter(completed_y_n=False)
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocerylist_lab01/index.html', context)

def add(request):
    new_description = request.POST['description']
    new_item = GroceryItem(description=new_description)
    new_item.save()
    return HttpResponseRedirect(reverse('grocerylist_lab01:index'))

def complete(request, pk):
    new_item = get_object_or_404(GroceryItem, pk=pk)
    new_item.completed = True
    new_item.completed_date = timezone.now()
    new_item.save()
    return HttpResponseRedirect(reverse('grocerylist_lab01:index'))

def delete(request, pk):
    new_item = get_object_or_404(GroceryItem, pk=pk)
    new_item.delete()
    return HttpResponseRedirect(reverse('grocerylist_lab01:index'))
