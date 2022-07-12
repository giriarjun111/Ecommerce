from django.apps import AppConfig
from allauth.account.signals import user_signed_up
from django.dispatch import receiver


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        from .models import Customer

        @receiver(user_signed_up)
        def create_customer_profile(sender, **kwargs):
            u = kwargs['user']
            customer = Customer.objects.create(
                user=u,
                name = f'{u.first_name} {u.last_name}',
                email = u.email
            )
