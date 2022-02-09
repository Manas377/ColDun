from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    market_cap = models.IntegerField()
    price = models.FloatField()
    country = models.CharField(max_length=50)
    