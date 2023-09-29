import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
# from django.dispatch import Signal

from products.models import Product
from profiles.models import UserAccount

# from .signals import order_created


class Order(models.Model):
    order_number = models.CharField(max_length=25, null=False, editable=False)
    user_account = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    name = models.CharField(max_length=50, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=25, null=False, blank=True)
    postcode = models.CharField(max_length=10, null=False, blank=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    def _order_number(self):
        '''Generates a unique order number'''

        return uuid.uuid4().hex.upper()

    def update_total_cost(self):
        """
        Update grand total each time a line item is added,
        including delivery.        """

        self.delivery_fee = self.order_total * \
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
        self.grand_total = self.order_total + self.delivery_fee
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)  
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'pk {self.product.pk} on order {self.order.order_number}'
