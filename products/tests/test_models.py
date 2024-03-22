'''
This file contains the tests for the Products model.
'''
import datetime

from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from products.models import Product, ProductCategory
from suppliers.models import Supplier


class ProductTest(TestCase):
    '''
    Test case for the Product model
    '''
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Supplier 1")

        self.category = ProductCategory.objects.create(
            name="Category 1",
        )

        self.product = Product.objects.create(
            name="Product 1",
            sku="12345678901234",
            price=9.99,
            stock=10,
            category=self.category,
            release_date=datetime.date.today(),
            supplier=self.supplier
        )

    def test_if_product_has_correct_fields(self):
        '''
        Test if the product has the correct fields
        '''
        self.assertEqual(self.product.name, "Product 1")
        self.assertEqual(self.product.sku, "12345678901234")
        self.assertEqual(self.product.price, 9.99)
        self.assertEqual(self.product.stock, 10)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.release_date, datetime.date.today())

        # Test if the slug is generated correctly
        self.assertEqual(self.product.slug, "product-1")
