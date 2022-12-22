from django.db import models

from datetime import datetime

# Create your models here.


# Here, each model is represented by a class that subclasses django.db.models.Model. 
# Each model has a number of class variables, each of which represents a database 
# field in the model.
class GroceryItem(models.Model):
    text_desc = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', default=datetime.now())
    completed_date = models.DateTimeField('date completed', default=datetime.now())
    # Is this where I would add a function to determine if it's complete??
    is_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.text_desc
