from django.db import models

from datetime import datetime


class GroceryItem(models.Model):
    text_desc = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', default=datetime.now())
    completed_date = models.DateTimeField('date completed', default=datetime.now())
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.text_desc