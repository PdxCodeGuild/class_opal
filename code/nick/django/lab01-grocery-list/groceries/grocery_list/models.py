from django.db import models

# Create your models here.


class Item(models.Model):
    item_text = models.CharField(max_length=150)
    creation_date = models.DateTimeField('date created', auto_now=True)
    completed_date = models.DateTimeField(
        'date completed', null=True, blank=True)
    completed = models.BooleanField()
