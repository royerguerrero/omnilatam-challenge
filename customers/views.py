"""Customers views"""

# Django
from django.contrib.auth.views import LoginView


class SingInView(LoginView):
    template_name = 'login.html'
