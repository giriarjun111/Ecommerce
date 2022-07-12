from .models import Customer
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def createCustomerProfile(sender=User, **kwargs):
    
    customer = Customer.objects.create(
        name = user.first_name,
    )

