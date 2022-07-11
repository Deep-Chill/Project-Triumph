from django.contrib import admin
from .models import CountryPresident, SupremeCourt, Mayor,  Embargos, CountryRelations

admin.site.register(CountryPresident)
admin.site.register(SupremeCourt)
admin.site.register(Mayor)
admin.site.register(Embargos)
admin.site.register(CountryRelations)
# Register your models here.
