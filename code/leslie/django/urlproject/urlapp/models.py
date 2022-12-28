from django.db import models


class Url(models.Model):
    long_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=20, unique=True, blank=True)

    def __str__(self) -> str:
        return f"Long Url: {self.long_url}; Short Url code: {self.short_code}"
