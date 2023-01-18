from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from common.code_generator import code_generator
from django.urls import reverse
from .models import Url
# Create your views here.


def index(request):
    return render(request, 'url_manager/index.html')


def generate(request):
    new_url = Url.objects.create(original_url=request.POST['url'])
    new_url.code = code_generator()
    new_url.save()
    return render(request, 'url_manager/index.html', {'new_url': new_url})


def redirect(request, get_code):
    url = Url.objects.get(code=get_code).original_url
    return HttpResponseRedirect(url)
