from django.shortcuts import render
from django.views.generic.list import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #keeps the server from going to reverse right away before importing the URLs in the classes - reverse_lazy won’t evaluate until the value is needed
from .models import Post

class BlogListView(ListView): #general read view
    model = Post
    template = 'home.html'

class BlogDetailView(DetailView): #this is the read view for a specific post
    model = Post
    template = 'post_detail.html'

#create, update & delete views have auto-generated views, just specify which fields you want (dates are added automatically) 
class BlogCreateView(CreateView): #handles both POST & GET
    model = Post
    template = 'post_new.html'
    fields = ['title', 'author', 'body'] #fields are shown on page according to how they are ordered here

class BlogEditView(UpdateView):
    model = Post
    fields = ['title', 'body'] #the post is already tied to the user name so no need to add the author field
    template = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:home')
    template = 'post_delete.html'   