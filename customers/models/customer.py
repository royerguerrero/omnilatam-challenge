"""Customer models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO: add phone number validator
    number_phone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns customer's name"""
        return str(self.user.get_full_name())

