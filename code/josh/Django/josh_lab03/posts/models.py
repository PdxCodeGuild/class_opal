from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    chirp = models.CharField(max_length=128)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)

    def __str__(self):
        return(f'{self.chirp}, {self.users}, {self.pub_date}')