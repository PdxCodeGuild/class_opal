from django.db import models

class BothUrls(models.Model):
    long_url = models.URLField(_(""), max_length=200)
    short_code = models.URLField(_(""), max_length=20)

    def __str__(self):
        return self.short_code