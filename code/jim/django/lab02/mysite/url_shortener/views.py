from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Url
from .url_converter import get_code


def index(request):
    # TODO this page needs to display the code associated with the url the user just entered
    # add a url = None argument to this function and have submit url pass the submitted url?
    urls = Url.objects.all()
    return render(request, 'url_shortener/index.html', {'urls': urls})


def submit_url(request):
    long_url = request.POST['long_url']
    code = get_code()
    Url.objects.create(code=code, url=long_url)
    return HttpResponseRedirect(reverse('url_shortener:index'))


def redirect_user(request, code):
    url = Url.objects.get(code=code).url
    return HttpResponseRedirect(url)
