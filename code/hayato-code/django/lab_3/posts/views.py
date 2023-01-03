from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Post
from django.http import Http404

# home view to show all posts on home page
def home(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts":posts})


# view to create a post
@login_required
def add_post(request):
    if request.method == "POST":
        # if user is submitting the post form
        form = AddPostForm(request.POST, request.FILES)  

        if form.is_valid():
            # if the form is valid
            # save form but don't commit to database
            post = form.save(commit=False)
            
            # add the current logged in user as the one who uploaded the post
            post.uploaded_by = request.user
             
            # save the post
            post.save()
            
            # return the user to their profile page
            return redirect(reverse("profile", args=(request.user.id,)))
        else:
            print(form.errors)
    else:
        form = AddPostForm()
    
    return render(request, "posts/add-post.html", {"form":form})






@login_required
def delete_post(request,pk):
    try:
        post = Post.objects.get(id=pk)

        if request.user == post.uploaded_by:
            # if the one deleting is the owner of the post
            post.delete()

            
            return redirect(reverse("profile", args=(request.user.id,)))

    except Post.DoesNotExist:
        raise Http404