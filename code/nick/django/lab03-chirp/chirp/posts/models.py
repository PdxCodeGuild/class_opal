from django.db import models
from users.models import User

# Create your models here.


class Post(models.Model):
    post_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    comment_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
