from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'delivery_fee',
                       'grand_total',)

    fields = ('order_number', 'user_profile', 'date', 'name',
              'street_address1', 'street_address2', 'county',
              'postcode', 'phone_number', 'email',
              'delivery_fee', 'order_total', 'grand_total',)

    list_display = ('order_number', 'name', 'date',
                    'order_total', 'delivery_fee',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
