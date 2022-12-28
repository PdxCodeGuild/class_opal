import random
from string import ascii_letters as letters, digits as digits
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import UrlShortener


def index(request):
    if request.method == 'POST':
        form_data = request.POST
        all_characters = letters + digits
        code = []
        while len(code) < 10:
            code.append(random.choice(all_characters))
        code_join = "".join(code)
        url = UrlShortener.objects.create(
            long_url=form_data['long_url'], 
            short_code = code_join
        )
        return HttpResponseRedirect(reverse('url_shortener:index'))
    else:
        url = UrlShortener.objects.all()
        context = {'url_shortener': url}
        return render(request, 'url_shortener/index.html', context)


def redirect(request, id):
    url = UrlShortener.objects.get(id=id)
    return HttpResponseRedirect(url.long_url)