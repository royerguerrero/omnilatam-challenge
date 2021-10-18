"""Customers Serializers"""

# Django Rest Framework
from django.db.models import fields
from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from customers.models import Customer, ShippingAddress, Notification
from orders.models import Order

# Serializers
from orders.serializers import OrderSerializer 


class UserSerializer(serializers.ModelSerializer):
    """It's the serializer for hyperlink with customer serializer."""
    class Meta:
        """User serializer meta class."""
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'))
        instance = Customer.objects.create(user=user, **validated_data)
        return instance


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'