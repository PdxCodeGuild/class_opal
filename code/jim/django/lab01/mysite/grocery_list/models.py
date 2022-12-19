from django.db import models


class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    completed_date = models.DateTimeField('date completed')
    is_complete = models.BooleanField('is complete')

    def __str__(self):
        return self.description
