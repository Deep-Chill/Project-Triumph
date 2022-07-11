from django.db import models
from django.db.models.functions import Greatest, Least
from Location.models import Country
from User.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator

### Need to ensure the Enemy and Ally models don't insert duplicates, or opposite relationships via code in
# the front end

# class Enemy(models.Model):
#     country_1 = models.ForeignKey(Country, on_delete=models.CASCADE)
#     country_2 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='enemy_country')
#     declaration_date = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['country_1', 'country_2', 'declaration_date'], name='unique_enemies')
#         ]

# class Ally(models.Model):
#     country_1 = models.ForeignKey(Country, on_delete=models.CASCADE)
#     country_2 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='allied_country')
#     declaration_date = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['country_1', 'country_2', 'declaration_date'], name='unique_allies')
#         ]


class Embargos(models.Model):
    sender = models.ForeignKey(Country, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='embargoed_country')
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['sender', 'receiver', 'date'], name='unique_embargo')
        ]
#Implemented national policies into the existing country model

# class NationalPolicies(models.Model):
#     government_types = (
#         ('DE', 'democracy'),
#         ('DD', 'direct democracy'),
#         ('DC', 'dictatorship')
#     )
#     country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='national_policies')
#     income_tax = models.DecimalField(max_digits=4, decimal_places=2, default=1,
#                                      validators=[MaxValueValidator(100), MinValueValidator(0)])
#     sales_tax = models.DecimalField(max_digits=4, decimal_places=2, default=1,
#                                     validators=[MaxValueValidator(100), MinValueValidator(0)])
#     import_tax = models.DecimalField(max_digits=4, decimal_places=2, default=1,
#                                      validators=[MaxValueValidator(100), MinValueValidator(0)])
#     trade_license_fees = models.IntegerField(default=0)
#     minimum_wage = models.DecimalField(max_digits=4, decimal_places=2, default=0)
#     free_trade_agreements = models.ManyToManyField(Country, symmetrical=True)
#     government_type = models.CharField(max_length=100, choices=government_types)
#

class CountryRelations(models.Model):
    country_relations = (('al', 'Ally'), ('nt', 'Neutral'), ('en', 'Enemy'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    target = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    relation = models.CharField(max_length=20, choices=country_relations)

class CountryPresident(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    president = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('country', 'president'),)

class Mayor(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

class SupremeCourt(models.Model):
    country = models.OneToOneField(Country, on_delete=models.CASCADE)
    size = models.IntegerField()
    members = models.ForeignKey(Profile, on_delete=models.CASCADE)
