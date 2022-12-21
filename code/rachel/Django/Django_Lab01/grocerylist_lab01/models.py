from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed_y_n = models.BooleanField(default=False)

    def __str__(self):
        return self.description


