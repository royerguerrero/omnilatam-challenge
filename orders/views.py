"""Orders views"""

# Django Rest Framework
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

# Models
from orders.models import Order, Shipping, Payment

# Serializers
from orders.serializers import OrderSerializer, PaymentSerializer, ShippingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['customer', 'shipping_address',]
    search_fields = ['customer__id', 'shipping_address', 'created_at', 'updated_at',] 


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer 
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['payment_method', 'approved', 'order', 'order__customer__id', 'created_at', 'updated_at',]
    search_fields = ['order'] 


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer 
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['shipping_address', 'status', 'created_at', 'updated_at',]
    search_fields = ['observations'] 