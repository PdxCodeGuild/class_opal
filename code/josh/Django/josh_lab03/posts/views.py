from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import Posts
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        form_data = request.POST
        user = User.objects.filter(username=request.user)
        post = Posts.objects.create(
            chirp = form_data['chirp'],
            users = user[0]
        )
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        post = Posts.objects.all()
        print('Testing.')
        print(post)
        user = User.objects.filter(username=request.user)
        print(user)
        context = {'posts': post}
        return render(request, 'posts/index.html', context)