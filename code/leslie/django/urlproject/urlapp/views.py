from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
import random
import string
from .models import Url


def index(request):
    return render(request, 'index.html')


def createshorturl(request):
    if request.POST:
        # creates short url code -- 7 random chars in string
        short_code = ''.join(random.choice(string.ascii_letters)
                             for x in range(7))
        long_url = request.POST['long_url']
        new_url = Url(long_url=long_url, short_code=short_code)
        new_url.save()
        return HttpResponseRedirect('/')


def url_created(request):
    url = Url.objects.all()
    list_of_short_urls = []
    # turned list_of_short_urls into a dictionary so all 3 args could be added
    for x in url:
        list_of_short_urls.append({'short_code': str(
            x.short_code), 'long_url': x.long_url, 'times_clicked': x.times_clicked})
    print(list_of_short_urls)
    return render(request, 'detail.html', {'url': list_of_short_urls})


def direct_user(request, short_code):
    try:
        short_url = Url.objects.get(short_code=short_code)
        print("short_url")
        short_url.times_clicked += 1
        short_url.save()
        return HttpResponseRedirect(short_url.long_url)
    except:
        raise Http404('This URL not found!')
