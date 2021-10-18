"""Customers views"""

# Django Rest Framework
from django.views.generic import detail
from rest_framework import permissions, serializers, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from customers.models import Customer, ShippingAddress, Notification

# Serializers
from customers.serializers import CustomerSerializer, ShippingAddressSerializer, NotificationSerializer

# Permissions
from customers.permissions import isUserOwner


class CustomerViewSet(viewsets.ModelViewSet):
    """Viewset for customer endpoints."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__email']

    @action(detail=True, methods=['get'])
    def notifications(self, request, pk=None):
        """Return notification's user"""
        data = Notification.objects.filter(customer=pk) 
        serializer = NotificationSerializer(data, many=True)

        return Response(serializers.data)

    @action(detail=True, methods=['get', 'put', 'delete'])
    def shipping_address(self, request, pk=None):
        """List the shipping address for user or create one."""
        data = ShippingAddress.objects.filter(customer=pk)
        serializer = ShippingAddressSerializer(data=data, many=True)

        return Response(serializer.data)