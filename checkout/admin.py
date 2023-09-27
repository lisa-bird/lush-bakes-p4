from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'order_total', 'delivery_fee',
                       'grand_total',)

    fields = ('name', 'street_address1', 'street_address2',
              'county', 'postcode', 'phone_number', 'email',)

    list_display = ('order_number', 'date', 'name', 
                    'order_total', 'delivery_fee',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
