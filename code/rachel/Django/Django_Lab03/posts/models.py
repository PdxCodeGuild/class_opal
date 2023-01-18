from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=128)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE) #auth.user = link the post to the user/author; related_name = look up posts according to author; cascade = delete everything that's under (related) to the author
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,)) #HTTP response redirect (to post's details page)
    
    class Meta:
        ordering = ['-created']