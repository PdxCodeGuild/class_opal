from django.shortcuts import get_object_or_404, render
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


def delete(request, item_id):
    item_to_delete = get_object_or_404(Item, pk=item_id)


def completer(request):
    ...


def create(request):
    ...
