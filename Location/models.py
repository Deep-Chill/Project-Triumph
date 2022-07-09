from django.db import models
import datetime

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    sales_tax = models.DecimalField(max_digits=4, decimal_places=2)
    income_tax = models.DecimalField(max_digits=4, decimal_places=2)
    gold_amount = models.IntegerField(default=0)
    Currency_amount = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    @property
    def user_count(self):
        return self.profile_set.count()
    '''return the currency of this country'''
    @property
    def currency(self):
        return self.currency_set.first()

class Region(models.Model):
    '''each country has many regions'''
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default='', related_name='region_set')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    def __str__(self):
        return self.name
    '''return number of users in this region'''
    @property
    def num_users(self):
        return self.profile_set.count()

class City(models.Model):
    fortification_choices = (
        ('BW', 'Basic Wall'),
        ('FW', 'Fortified Wall'),

    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fortification = models.CharField(max_length=2, choices=fortification_choices)
