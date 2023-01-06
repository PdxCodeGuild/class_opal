# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     follows = models.ManyToManyField(
#         "self",
#         related_name="followed_by",
#         symmetrical=False,
#         blank=True
#     )