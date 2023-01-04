from django.shortcuts import render, HttpResponse
from .models import Comment, Like, Post
# Create your views here.


def index(request):
    post_feed = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/index.html', {'post_feed': post_feed})


def like(request, post_id):
    Like.objects.create()
    ...


def comments(request):
    ...
