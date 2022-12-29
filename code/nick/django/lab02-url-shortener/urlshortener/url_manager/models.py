from django.db import models
from common.code_generator import code_generator

# Create your models here.


class Url(models.Model):
    original_url = models.CharField(max_length=255)
    code = models.CharField(max_length=12, default=code_generator())
