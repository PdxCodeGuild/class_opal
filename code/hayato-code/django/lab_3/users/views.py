"""
views for authentication
"""

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import User
from posts.models import Post
from posts.forms import AddPostForm
from django.http import Http404


@login_required
def login_redirect(request):
    """
    function to redirect user after login
    """
    return redirect(reverse("profile", args=(request.user.id,)))


def register(request):
    """
    view to handle users registration
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # if the form is valid save it
            form.save()

            # get the username and password from the form to log in user immediately after registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # authenticate the user
            user = authenticate(username=username, password=password)
            login(request, user)

            # redirect the user to their profile
            return redirect(reverse('profile', args=(user.id,)))
    else:
        form = RegistrationForm()

    context = {'form':form}

    return render(request, 'registration/register.html', context=context)



@login_required()
def profile(request, pk):
    """
    view to show the public profile of a user given their id
    """
    try:
        # get the user from the given id
        user = User.objects.get(id=pk)

        # get all posts of this user
        posts = Post.objects.filter(uploaded_by=user).order_by("-id")
        
        # create a form to show on the profile page to enable users to add a post
        form = AddPostForm()

        return render(request, "registration/profile.html", {"posts":posts, "form":form, "user_id":pk})
    except User.DoesNotExist:
        # if the user with given id does not exist raise a 404 error
        raise Http404

