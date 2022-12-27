from django.db import models

# Create your models here.
class Shorturl(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    
    def __str__(self):
        return self.code
