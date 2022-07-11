from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from Location.models import Country, Region
from Currencies.models import Currency

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    health = models.IntegerField(default=100)
    strength_n = models.IntegerField(default=0)
    strength = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    militaryrank = models.IntegerField(default=0)
    productivity = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    fairness = models.IntegerField(default=0)
    political_achievement = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(max_length=200)
    location = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, related_name='player_location')
    friends = models.ManyToManyField("Profile", blank=True, symmetrical=True)

    def save(self, *args, **kwargs):
        created = self._state.adding
        super(Profile, self).save(*args, **kwargs)
        if created:
            UserBalance.objects.create(user=self.user, currency=self.country.national_currency, Balance=0)

    def __str__(self):
        return f'{self.user.username}'
    def level(self):
        return self.xp // 10

class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    currency = models.ForeignKey(Currency, blank=True, on_delete=models.CASCADE)
    Balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.currency.symbol} balance"

    def increase_balance(self):
        self.Balance += 10
        self.save()

class CountryBalance(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)
    currency = models.ForeignKey(Currency, blank=True, on_delete=models.CASCADE)
    Balance = models.DecimalField(max_digits=10, decimal_places=2)

class Message(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
