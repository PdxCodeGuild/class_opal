from django.http import Http404
from django.shortcuts import render

from .models import GroceryItem


# Create your views here.
def index(request):
    latest_grocery_items = GroceryItem.objects.order_by('created_date')[:5]
    context = {
        'latest_grocery_items': latest_grocery_items,
    }
    # The render() function takes the request object as its first argument, a template name as its 
    # second argument and a dictionary as its optional third argument. It returns an HttpResponse 
    # object of the given template rendered with the given context.
    return render(request, 'grocery_list/index.html', context)

def detail(request, text_desc_id):
    try:
        text_desc = GroceryItem.objects.get(pk=text_desc_id)
    except GroceryItem.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'grocery_list/detail.html', {'text_desc': text_desc})