from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
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


def delete(request, item_id):
    item_to_delete = get_object_or_404(Item, pk=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))


def completer(request, item_id):
    item_to_complete = get_object_or_404(Item, pk=item_id)
    item_to_complete.completed = not item_to_complete.completed
    item_to_complete.save()
    if item_to_complete.completed == True:
        item_to_complete.completed_date = datetime.now()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def create(request):
    Item.objects.create(item_text=request.POST['item'])
    return HttpResponseRedirect(reverse('grocery_list:index'))
