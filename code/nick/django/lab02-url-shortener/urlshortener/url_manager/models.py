from django.db import models


# Create your models here.


class Url(models.Model):
    original_url = models.CharField(max_length=255)
    code = models.CharField(max_length=12, blank=True)

    def __str__(self) -> str:
        return f'http://127.0.0.1:8000/url_manager/redirect/{self.code}'
