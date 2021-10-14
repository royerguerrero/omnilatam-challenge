"""Customer models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

# Utils
from ecommerce_flow.constants import COUNTRIES_CHOICES

class Customer(models.Model):
    """Customer Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_phone = models.CharField(max_length=10)
    alternative_number_phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns customer's name"""
        return str(self.user.get_fullname())


class ShippingAddress(models.Model):
    """Shipping address Model"""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    country = models.CharField(max_length=100, choices=COUNTRIES_CHOICES)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=5, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the complete address"""
        return f'{self.address}, {self.city}({self.state}, {self.country}) {self.zip_code}'
