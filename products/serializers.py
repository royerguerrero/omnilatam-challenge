"""Products Serializers"""

# Django Rest Framework
from rest_framework import serializers

# Models
from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CaategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'
