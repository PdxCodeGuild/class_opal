from django.db import models

# Create your models here.
class Shorturl(models.Model):
    text_desc = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', default=datetime.now())
    completed_date = models.DateTimeField('date completed', default=datetime.now())
    # Is this where I would add a function to determine if it's complete??
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.text_desc
