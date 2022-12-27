from django.db import models


class GroceryItem(models.Model):
    item_description = models.CharField(max_length=300)
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField(
        blank=True, null=True)  # says field can be blank
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item_description
