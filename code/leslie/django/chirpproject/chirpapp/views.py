from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView


# def index(request):
#     user_chirps = Post.objects.order_by('-pub_date')[:5]
#     output = ','.join([c.content for c in user_chirps])
#     return HttpResponse(output)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    fields = ['content', 'author']
    template_name = 'chirpapp/new_post.html'
    success_url = '/'
