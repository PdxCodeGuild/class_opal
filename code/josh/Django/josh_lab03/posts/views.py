from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . models import Posts

def index(request):
    if request.method == 'POST':
        form_data = request.POST
        post = Posts.objects.create(
            chirp = form_data['chirp'], 
        )
        return HttpResponseRedirect(reverse('posts:index'))
    else:
        post = Posts.objects.all()
        context = {'posts': post}
        return render(request, 'posts/index.html', context)