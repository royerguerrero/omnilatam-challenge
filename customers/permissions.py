"""Customers Custom Permussions"""

# Django Rest Framework
from rest_framework import permissions

class isUserOwner(permissions.BasePermission):
    """Validates that the user is the user in order
    to view or modify his data.
    """
    def has_object_permission(self, request, view, obj):
        """Checks if the user id in the request is same as the user id in object user

        Returns:
            bool: This determine wheather or not the user has permission
            to perform action on the endpoint.
        """
        if request.user.id == obj.user.id:
            return True

        return False