from django.db import models
from common.url_generator import url_generator

# Create your models here.


class Url(models.Model):
    original_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=15, default=url_generator())
