"""Products views"""

# Django
from django.shortcuts import render

# Django Rest Framework
from rest_framework import viewsets, permissions

# Serializers
from products.serializers import ProductSerializer

# Models
from products.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    """Products API ViewSet"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class CategoryViewSet(viewsets.ModelViewSet):
    """Category API ViewSet"""
    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAuthenticated]
