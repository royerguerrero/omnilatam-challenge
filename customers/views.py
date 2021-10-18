"""Customers views"""

# Django Rest Framework
from rest_framework import permissions, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Models
from customers.models import Customer, ShippingAddress

# Serializers
from customers.serializers import CustomerSerializer, ShippingAddressSerializer

# Permissions
from customers.permissions import isUserOwner


class CustomerViewSet(viewsets.ModelViewSet):
    """Viewset for customer endpoints."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'user__email']

    @action(detail=True, methods=['get', 'put', 'delete'])
    def shipping_address(self, request, pk=None):
        """List the shipping address for user or create one."""
        data = ShippingAddress.objects.filter(customer=pk)
        serializer = ShippingAddressSerializer(data=data, many=True)

        return Response(serializer.data)