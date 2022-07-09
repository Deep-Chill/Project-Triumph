from django.contrib import admin
from .models import NationalPolicies, CountryPresident, SupremeCourt, Mayor, Enemy, Ally

admin.site.register(NationalPolicies)
admin.site.register(CountryPresident)
admin.site.register(SupremeCourt)
admin.site.register(Mayor)
admin.site.register(Ally)
admin.site.register(Enemy)
# Register your models here.
