from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hellow, world. You're at the grocery list.")