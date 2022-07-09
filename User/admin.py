from django.contrib import admin
from .models import Profile, UserBalance

# Register your models here.

admin.site.register(Profile)
admin.site.register(UserBalance)