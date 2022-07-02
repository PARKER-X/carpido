from django.apps import AppConfig
import imp

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


    def ready(self):
        from django.contrib.auth.models import User
        def get_cart_count(self):
            from .models import CartItems
            return CartItems.objects.filter(cart__is_paid=False, cart__user= self).count()

        User.add_to_class("get_cart_count",get_cart_count)
