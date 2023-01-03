from django import forms
from .models import Post

# form to add posts
class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("image","content")
