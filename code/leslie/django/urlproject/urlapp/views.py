from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from django.template import loader
import random
import string
from .models import Url


# class IndexView(generic.ListView):
#     template_name = 'urlapp/index.html'
# context_object_name = 'Url_list'

# def get_queryset(self):
# return Url.objects.order_by('-date_created')[:10]


def index(request):
    return render(request, 'index.html')


def createshorturl(request):
    if request.POST:
        # creates short url code -- 7 random chars in string
        short_code = "".join(random.choice(string.ascii_letters)
                             for x in range(7))
        long_url = request.POST['long_url']
        new_url = Url(long_url=long_url, short_code=short_code)
        new_url.save()
        return HttpResponseRedirect('/')


def url_created(request):
    url = Url.objects.all()
    return render(request, 'detail.html', {'url': url})


def redirect(request, short_code):
    try:
        short_url = Url.objects.get(short_code=short_code)
        short_url.save()
        return HttpResponseRedirect(short_url.long_url)
    except:
        raise Http404('No URL found!')
