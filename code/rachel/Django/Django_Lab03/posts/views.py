from django.shortcuts import render
from django.views.generic.list import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView): #general read view
    model = Post
    template = 'home.html'

class BlogDetailView(DetailView): #this is the read view for a specific post
    model = Post
    template = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['name', 'title', 'post']

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['name', 'title', 'post']
    template = 'edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('author-list')   