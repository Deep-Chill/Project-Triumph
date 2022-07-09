from django.db import models
from Location.models import Country
from django.contrib.auth.models import User

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    country = models.OneToOneField(Country, on_delete=models.CASCADE, default='', related_name='national_currency')
    def __str__(self):
        return self.name


class Gold(models.Model):
    name = models.CharField(max_length=100, default='Gold')
    symbol = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'