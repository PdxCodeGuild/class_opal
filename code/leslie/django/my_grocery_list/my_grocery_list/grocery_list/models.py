from django.db import models


class GroceryItem(models.Model):
    item_description = models.CharField(max_length=300)
    date_created = models.DateField('date created')
    date_completed = models.DateField('date completed')
    is_complete = models.BooleanField()

    def __str__(self):
        return self.item_description
