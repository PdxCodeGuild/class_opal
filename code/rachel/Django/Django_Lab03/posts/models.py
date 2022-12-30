from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    blog_text = models.CharField(max_length=128)
    author = models.CharField(max_length=20)
    edit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
