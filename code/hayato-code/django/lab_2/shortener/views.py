from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Shortened
from .forms import UrlShortenerForm


def home(request):
    form = UrlShortenerForm(request.POST or None)

    if request.method == 'GET':
        # if it is a get request show the form to the user
        return render(request, "shortener/home.html", {"form":form})

    elif request.method == 'POST':
        # if user is submitting the form

        if form.is_valid():
            # if the form is valid and user has entered a valid url
            shortened = form.save()

            long_url = shortened.url
            
            # request.build_absolute_uri('/') this will return the complete
            # url the request was sent on so if you deploy and pay for  domain
            # this will return the domain for example https://shortner.com
            # but for now this will return http://localhost:8000
            short_url = request.build_absolute_uri('/') + shortened.code 
             
            #  send the long url , short url and form to be shown to user
            return render(request, "shortener/home.html", {"long_url":long_url, "short_url":short_url, "form":form})

        # if user entered an invalid url send errors to show
        return render(request, "shortener/home.html", {"errors":form.errors})


def redirect_user(request, code):
    # view to redirect user
    try:
        # if we have a url with the shorted code given redirect
        shortened = Shortened.objects.get(code=code)
        return HttpResponseRedirect(shortened.url)
    except:
        # if we do not have a url with the shorted code show that the code is invalid
        raise Http404('URL not found')
