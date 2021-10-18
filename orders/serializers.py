"""Order Serializers"""

# Django Rest Framework
from django.forms import fields
from rest_framework import serializers

# Models
from orders.models import Order, Payment, Shipping


class OrderSerializer(serializers.ModelSerializer):
    """Order Serializer"""
    class Meta:
        """Order Serializer meta class"""
        model = Order
        fields = '__all__' 

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = '__all__'