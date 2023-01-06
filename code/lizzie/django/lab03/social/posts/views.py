from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Post, User
# Create your views here.


def index(request):
    '''
    Renders the homepage with user posts displayed.
    '''
    posts = Post.objects.all()
    context = {'posts': posts}
    # Rendering the home html page with all the posts passed as context.
    return render(request, 'home.html', context)


def add_post(request):
    '''
    Creates new post object to be included on homepage.
    '''
    post_text = request.POST['new_post']
    Post.objects.create(user=request.user, post_text=post_text)
    return HttpResponseRedirect(reverse('posts:index'))


def user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'userposts.html', {'user':user})