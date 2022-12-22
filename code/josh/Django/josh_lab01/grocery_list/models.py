from django.db import models


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    completed_date = models.DateTimeField('completed date')
    completed = models.BooleanField()

    def __str__(self):
        return self.grocery_list