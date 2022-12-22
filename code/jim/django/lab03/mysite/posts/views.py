from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Post


def index(request):
    post_list = Post.objects.all()
    context = {'posts': post_list}
    return render(request, 'home.html', context)


def add_post(request):
    post_text = request.POST['new_post']
    new_post = Post.objects.create(user=request.user, post_text=post_text)
    return HttpResponseRedirect(reverse('posts:index'))
