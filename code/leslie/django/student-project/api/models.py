from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=50)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=50)
    capstone = models.URLField(max_length=200)

    def __str__(self):
        return self.first_name
