from django.db import models
from User.models import Profile
from Business.models import Company

class weaponRawMaterial(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    def add_quantity(self, x):
        self.quantity += x
        self.save()
    def remove_quantity(self, x):
        self.quantity -= x
        self.save()

    def __str__(self):
        return self.name
    def create_weaponRawMaterial(self, name, price):
        self.name = name
        self.price = price
        self.save()
