from django.shortcuts import render
from django.views.generic.list import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template = home.html

class BlogDetailView(DetailView):
    model = Post
    template = detail.html

class BlogCreateView(CreateView):
    model = Post
    fields = ['name', 'title', 'post']