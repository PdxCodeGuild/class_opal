from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    post_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_post = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)


class Comment(models.Model):
    comment_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)
