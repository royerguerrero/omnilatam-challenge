"""Customers test"""

# Django
from django.urls import reverse

# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Models
from customers.models import Customer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Mommy Mocks
from model_mommy import mommy


class CustomerViewSetTestCase(APITestCase):
    url = reverse('customers_viewset-list')
    customers = []

    def setUp(self):
        """Create a user and expose to client the token for use the api."""
        self.user = User.objects.create(
            username='elon', email='elon@spacex.com', password='s3xy',
            first_name='Elon', last_name='Musk', is_staff=True,
        )
        self.token = Token.objects.create(user=self.user)

        Customer.objects.create(id=999, user=self.user,
                                number_phone='00 000 000')
        self.mock_customers()

    def mock_customers(self):
        for _ in range(20):
            self.customers.append(mommy.make('customers.Customer'))

    def get_detail_url(self, pk):
        """Returns a customer url endpoint for detail.
        Args:
            pk (string): customer id.

        Returns:
            str: customer url detail.
        """
        return reverse('customers_viewset-detail', kwargs={'pk': pk})

    def api_authentication(self):
        """Includes in self.client the token for can make requests"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_can_create_customer(self):
        data = {
            'user': {
                'username': 'steve',
                'first_name': 'Steve',
                'last_name': 'Jobs',
                'email': 'ceo@apple.com',
            },
            'number_phone': '01 800 0000 0000'
        }

        response = self.client.post(self.url, data, format='json')
        user = response.data['user']

        self.assertEqual(user['first_name'], 'Steve')
        self.assertEqual(user['last_name'], 'Jobs')
        self.assertEqual(user['email'], 'ceo@apple.com')
        self.assertEqual(response.data['number_phone'], '01 800 0000 0000')

    def test_can_list_customers(self):
        customers_count = Customer.objects.count()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(customers_count, response.data['count'])

    def test_can_get_customer(self):
        response = self.client.get(self.get_detail_url(999))
        user = response.data['user']

        self.assertEqual(response.data['id'], 999)
        self.assertEqual(user['first_name'], 'Elon')
        self.assertEqual(user['last_name'], 'Musk')
        self.assertEqual(user['email'], 'elon@spacex.com')
        self.assertEqual(response.data['number_phone'], '00 000 000')

    def test_can_update_customer(self):
        pass

    def test_can_delete_customer(self):
        customers_count = Customer.objects.count()
        response = self.client.delete(self.get_detail_url(999))
        self.assertEqual(customers_count - 1, Customer.objects.count())
        self.assertRaises(
            Customer.DoesNotExist,
            Customer.objects.get, id=999
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_add_customer_shipping_address(self):
        pass

    def test_can_update_customer_shipping_address(self):
        pass

    def test_can_list_customer_shipping_address(self):
        pass

    def test_can_delete_customer_shipping_address(self):
        pass
