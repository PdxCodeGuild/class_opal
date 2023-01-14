from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class PersonalizedIndex(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    index_allocation = models.IntegerField()
    market_cap_min = models.IntegerField()
    dividend_yield_min = models.FloatField()
    pe_ratio_max = models.FloatField()
    sector_exclude_1 = models.CharField(max_length=200)
    sector_exclude_2 = models.CharField(max_length=200)
