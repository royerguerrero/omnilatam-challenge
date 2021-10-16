"""Products tests"""

# Django Rest Framework
from rest_framework.test import APITestCase

# Models
from products.models import Product, Category


class ProductCreateTestCase(APITestCase):
    def setUp(self):
        Category.objects.create(name='Books')        

    def test_create_product(self):
        total_products_count = Product.objects.count()

        product_propierties = {
            'name': 'From Animals into Gods: A Brief History of Humankind',
            'description': 'About 100,000 years ago, Homo sapiens was still an insignificant animal minding its own business in a corner of Africa. Our ancestors shared the planet with at least five other human...',
            'price': 14.77, 
            'category': 1,
            'stock': 30,
            'published': True
        }
        
        response = self.client.post('/api/products/', product_propierties)
        if response.status_code != 200:
            print(response.data)

        self.assertEqual(Product.objects.count(), total_products_count + 1)

