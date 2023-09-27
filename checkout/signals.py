from django.dispatch import Signal
from django.dispatch import receiver
from checkout.signals import order_created

order_created = Signal(providing_args=["order"])


@receiver(order_created)
def handle_order_created(sender, **kwargs):
    order = kwargs.get("order")
    # Perform actions based on the order creation event
    print("New order created:", order.order_number)