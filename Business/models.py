from django.db import models
from User.models import Profile

company_choices = (
    ('Weapon', 'Weapon'),
    ('Food', 'Food'),
    ('Real Estate', 'Real Estate'),
    ('Trading', 'Trading'),
    ('Other', 'Other'),
)

class Company(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=company_choices)
    description = models.TextField(null=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    raw_material = models.IntegerField(default=0)
    raw_material_price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Weapon_Company(Company):
    pass


class ShareHolders(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='')
    shareholder = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    share_count = models.IntegerField(default=0)
    def __str__(self):
        return self.shareholder.username
    def add_share(self, x):
        self.share_count += x
        self.save()
    def remove_share(self, x):
        self.share_count -= x
        self.save()
