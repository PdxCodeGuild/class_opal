from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Shorturl
from .url_converter import convert_url


# Create your views here.
def index(request):
    urls = Shorturl.objects.all()
    return render(request, 'urlshortener/index.html', {'urls': urls})


def submit_url(request):
    # Retrieve long_url from form
    long_url = request.POST['long_url']
    # Use custom function to convert long url to short code.
    code = convert_url(5)
    Shorturl.objects.create(code=code, url=long_url)
    return HttpResponseRedirect(reverse('urlshortener:index'))


def redirect_user(request, code):
    url = Shorturl.objects.get(code=code).url
    return HttpResponseRedirect(url)
