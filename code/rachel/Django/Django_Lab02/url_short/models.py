from django.db import models

class BothUrl(models.Model):
    long_url = models.CharField(max_length=200)
    short_code = models.CharField(max_length=20)

    def __str__(self):
        return self.short_code