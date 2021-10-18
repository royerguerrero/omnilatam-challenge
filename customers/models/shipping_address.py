"""Shipping address Model"""

# Django
from django.db import models

# Models
from customers.models import Customer

# Utils
from ecommerce_flow.constants import COUNTRIES_CHOICES

class ShippingAddress(models.Model):
    """Shipping address Model"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    country = models.CharField(max_length=3, choices=COUNTRIES_CHOICES)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'shipping address'

    def __str__(self):
        """Returns the complete address"""
        return f'{self.address}, {self.city}({self.state}, {self.country}) {self.zip_code}'
