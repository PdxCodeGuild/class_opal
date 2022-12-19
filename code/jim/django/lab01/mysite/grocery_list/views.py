from django.shortcuts import render

from .models import GroceryItem


def index(request):
    latest_grocery_item_list = GroceryItem.objects.order_by('-created_date')
    context = {'latest_grocery_item_list': latest_grocery_item_list}
    return render(request, 'grocery_list/index.html', context)
