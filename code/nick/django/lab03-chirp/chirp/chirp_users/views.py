from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'chirp_users/index.html')


def create(request):
    User.objects.create_user(
        username=request.POST['username'], email=None, password=request.POST['password'])
    return HttpResponseRedirect(reverse('posts:index'))
