from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items,
    }
    return render(request, 'grocery_list/index.html', context)

def add(request):
    description = request.POST("text_description")
    #GroceryItem.objects.create(text_description=description)
    item = GroceryItem(text_description=description)
    item.save()
    return HttpResponseRedirect(reverse("grocery_list:index"))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.completed:
        item.completed = False
        item.completed_date = None
    else:
        item.completed = True
        item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))