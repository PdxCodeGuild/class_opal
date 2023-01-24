from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    cohort = models.CharField(max_length=20)
    fav_topic = models.CharField(max_length=30)
    fav_teacher = models.CharField(max_length=30)
    capstone = models.URLField

    def __str__(self):
        return self.first_name