"""Customers Admin Configuration"""

# Django
from django.contrib import admin

# Models
from customers.models import Customer, ShippingAddress, Notification


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ShippingAddress)
class ShippingAddressModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    pass
