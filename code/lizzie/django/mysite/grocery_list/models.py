from django.db import models

# Create your models here.


# Here, each model is represented by a class that subclasses django.db.models.Model. 
# Each model has a number of class variables, each of which represents a database 
# field in the model.
class GroceryItem(models.Model):
    text_desc = models.CharField(max_length=200)
    created_date = models.DateTimeField('create date')
    completed_date = models.DateTimeField('complete date')
    # I'll figure out how to fix this later!!! Don't get mad at me program!
    is_complete = models.BooleanField(null=False)