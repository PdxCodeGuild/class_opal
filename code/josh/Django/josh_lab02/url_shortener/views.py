import random
import string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import UrlShortener

def index(request):
    if request.method == 'POST':
        form_data = request.POST
        url = UrlShortener.objects.create(
            long_url=form_data['long_url'], 
            short_code=form_data['short_url']
        )
        return HttpResponseRedirect(reverse('url_shortener:index'))

    else:
        url = UrlShortener.objects.all()
        context = {'url_shortener': url}
        return render(request, 'url_shortener/index.html', context)

def redirect(request):
    url = UrlShortener.objects.get(id=id)
    # Create variables to hold the string methods containing letters, digits, and symbols.
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Concatenate "letters," "digits," and "symbols" variables to draw random values from a single string.
    all_characters = letters + digits + symbols
    # Create an empty list to store values for password
    password = []
    # Create a while loop that runs enough times to select enough values from the "all_characters" variable for the new password.
    while len(password) < 10:
    # Add values to the "password" list at random from the "all_characters" variable.
        password.append(random.choice(all_characters))

    # Create a new variable "password_join" to join all the items in the password list using an empty string.
    password_join = "".join(password)
    # Display the new password using an f-string with a message to the user and the new 
    # password. 
    print(password_join)
    return HttpResponseRedirect(reverse('url_shortener:index'))