from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class PersonalizedIndex(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    index_name = models.CharField(max_length=200, default='my_index')
    index_allocation = models.IntegerField()
    market_cap_min = models.IntegerField()
    dividend_yield_min = models.FloatField()
    pe_ratio_max = models.FloatField()
    sector_exclude_1 = models.CharField(max_length=200)
    sector_exclude_2 = models.CharField(max_length=200)

    def __str__(self):
        return self.index_name


class Stock(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    sector = models.CharField(max_length=200, null=True)
    long_business_summary = models.CharField(max_length=2500, null=True)
    country = models.CharField(max_length=200, null=True)
    short_name = models.CharField(max_length=200, null=True)
    trailing_eps = models.FloatField(null=True)
    forward_pe = models.FloatField(null=True)
    market_cap = models.FloatField(null=True)
    dividend_yield = models.FloatField(null=True)
    trailing_pe = models.FloatField(null=True)

    def __str__(self):
        return self.symbol
