from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    favorite_topic = models.CharField(max_length=200)
    favorite_teacher = models.CharField(max_length=200)
    capstone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
