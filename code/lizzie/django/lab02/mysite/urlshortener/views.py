from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'urlshortener/index.html')


def submit_url(request):
    # Retrieve long_url from form
    long_url = request.POST['long_url']
    # Use custom function to convert long url to short code.
    code = convert_url(5)