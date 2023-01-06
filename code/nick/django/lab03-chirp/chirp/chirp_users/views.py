from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'chirp_users/index.html')


def create(request):
    new_user = User.objects.create_user(
        request.POST['username'], ..., request.POST['password'])
    return HttpResponseRedirect('')
