from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Comment, Like, Post
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    post_feed = Post.objects.all().order_by('-pub_date')
    return render(request, 'posts/index.html', {'post_feed': post_feed})


def new_post(request):
    print(request.user)
    Post.objects.create(
        post_text=request.POST['post'], user=request.user)
    return HttpResponseRedirect(reverse('posts:index'))


def like(request, post_id):
    Like.objects.create()
    ...


def comments(request):
    ...
