from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

