from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    blog_text = models.TextField(max_length=128)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE) #auth.user = link the post to the user/author; related_name = look up posts according to author; cascade = delete everything that's under (related) to the author
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
