import datetime

from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('created date')
    completed_date = models.DateTimeField('completed date')
    completed = models.BooleanField()

    def __str__(self):
        return self.grocery_list

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)