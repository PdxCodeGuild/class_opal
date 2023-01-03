from django.contrib import admin
from .models import Post

# registering the post modal to show up in admin
admin.site.register(Post)