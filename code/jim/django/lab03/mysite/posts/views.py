from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Post, User


def index(request):
    posts = Post.objects.all()
    user = request.user
    filtered_posts = posts.filter(user_id=user.id)
    context = {'posts': filtered_posts}
    return render(request, 'home.html', context)


def add_post(request):
    post_text = request.POST['new_post']
    Post.objects.create(user=request.user, post_text=post_text)
    return HttpResponseRedirect(reverse('posts:index'))


def user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user-posts.html', {'user': user})
