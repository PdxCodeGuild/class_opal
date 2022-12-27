from django.db import models

class UrlShortener(models.Model):
    long_url = models.CharField(max_length=200)
    short_code = models.CharField(max_length=200)

    def __str__(self):
        return self.long_url