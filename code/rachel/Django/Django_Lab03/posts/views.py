from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #keeps the server from going to reverse right away before importing the URLs in the classes - reverse_lazy won’t evaluate until the value is needed
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class BlogListView(ListView): #general read view
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): #this is the read view for a specific post
    model = Post
    template_name = 'post_detail.html'

#create, update & delete views have auto-generated views, just specify which fields you want (dates are added automatically) 
class BlogCreateView(LoginRequiredMixin, CreateView): #handles both POST & GET
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body'] #fields are shown on page according to how they are ordered here; 'author' was removed since we added the form_valid function below
    def form_valid(self, form):
        form.instance.author = self.request.user # automatically makes the user who submitted the request, the author
        return super().form_valid(form) #go back to doing everything you were going to do anyway

class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body'] #the post is already tied to the user name so no need to add the author field
    template_name = 'post_edit.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:home')
    template_name = 'post_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
