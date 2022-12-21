from django.db import models


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('created date')
    completed_date = models.DateTimeField('completed date')
    completed = models.BooleanField()