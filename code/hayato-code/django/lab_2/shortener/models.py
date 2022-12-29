from django.db import models

# modal that will store all shorted urls along with the code for the short url
class Shortened(models.Model):
    url = models.URLField()
    
    # make code unique so that no two urls can have the same code
    code = models.CharField(max_length=6, unique=True, blank=True)

    def __str__(self):
        return self.code