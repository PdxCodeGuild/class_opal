from django.shortcuts import HttpResponse

from .models import GroceryItem


# Create your views here.
def index(request):
    latest_grocery_items = GroceryItem.objects.order_by('created_date')[:5]
    output = ','.join([i.text_desc for i in latest_grocery_items])
    return HttpResponse(output)

def detail(request, text_desc_id):
    return HttpResponse(f"You're looking at item {text_desc_id}.")