from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_currency_balance(sender, instance, created, **kwargs):
#     if created:
#         Amount.objects.create(user=instance)