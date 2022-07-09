from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, UserBalance
from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         print("Success!")

# @receiver(post_save, sender=Profile)
# def create_home_balance(sender, instance, created, **kwargs):
#     if created:
#         UserBalance.objects.create(user=instance)