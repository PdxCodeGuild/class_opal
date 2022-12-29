from django.db import models


class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    completed_date = models.DateTimeField(
        'date completed', null=True, default=None)
    is_complete = models.BooleanField('is complete', default=False)

    def __str__(self):
        return self.description
