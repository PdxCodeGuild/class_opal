from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem


def index(request):
    incomplete_items = GroceryItem.objects.filter(
        complete=False).order_by('date_created')
    completed_items = GroceryItem.objects.filter(
        complete=True).order_by('date_completed')
    # context is what it's called in database
    context = {
        'incomplete_items': incomplete_items,
        'completed_items': completed_items
    }
    # render puts stuff in db
    return render(request, 'grocery_list/index.html', context)


def add(request):
    new_item = GroceryItem.objects.create(
        item_description=request.POST['item_description'])
    # reverse means django figures out URL for me
    # type:ignore
    return HttpResponseRedirect(reverse('grocery_list:index'))


def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.complete:
        item.complete = False
        # item.date_completed = None
    else:
        item.complete = True
        item.date_completed = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
