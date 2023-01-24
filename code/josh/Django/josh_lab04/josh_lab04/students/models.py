from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cohort = models.CharField(max_length=50)
    favorite_topic = models.CharField(max_length=50)
    favorite_teacher = models.CharField(max_length=50)
    capstone = models.CharField(max_length=50)


    def __str__ (self):
        return f'''
        Student: {self.first_name} {self.last_name}
        Cohort: {self.cohort}
        Favorites: Topic - {self.favorite_topic} Teacher - {self.favorite_teacher}
        Capstone: {self.capstone}
        '''