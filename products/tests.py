'''
Test cases for the products app.
'''
import datetime
from django.test import TestCase

from products.models import Product, ProductCategory, ProductGroup, ProductGroupItem,\
    ProductReleaseDateHistory


class ProductModelTest(TestCase):
    '''
    Test cases for the Product model.
    '''
    def test_create_product(self):
        '''
        Test creating a product.
        '''
        product = Product.objects.create(
            name='Product 1',
            description='Description 1',
            release_date=datetime.date(2020, 1, 1),
            price=10.00,
        )
        self.assertEqual(product.name, 'Product 1')
        self.assertEqual(product.description, 'Description 1')
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.stock, 0)

    def test_create_product_release_date_history(self):
        '''
        Test creating a product release date history.
        '''
        product = Product.objects.create(
            name='Product 1',
            release_date=datetime.date(2020, 1, 1),
        )
        history = ProductReleaseDateHistory.objects.get(product=product)
        self.assertEqual(history.product, product)
        self.assertEqual(history.release_date, datetime.date(2020, 1, 1))

    def test_updated_product_release_date_history(self):
        '''
        Test updating a product release date history.
        '''
        product = Product.objects.create(
            name='Product 1',
            release_date=datetime.date(2020, 1, 1),
        )
        history = ProductReleaseDateHistory.objects.get(product=product)
        self.assertEqual(history.release_date, datetime.date(2020, 1, 1))

        # Update the product release date
        product.release_date = datetime.date(2020, 1, 2)
        product.save()

        # Check the release date history
        histories = ProductReleaseDateHistory.objects\
            .filter(product=product).order_by('release_date')
        self.assertEqual(histories.count(), 2)
        self.assertEqual(histories[0].release_date, datetime.date(2020, 1, 1))
        self.assertEqual(histories[1].release_date, datetime.date(2020, 1, 2))


    def test_create_product_category(self):
        '''
        Test creating a product category.
        '''
        category = ProductCategory.objects.create(
            name='Category 1',
        )
        self.assertEqual(category.name, 'Category 1')

    def test_create_product_group(self):
        '''
        Test creating a product group.
        '''
        group = ProductGroup.objects.create(
            name='Group 1',
        )
        self.assertEqual(group.name, 'Group 1')

    def test_create_product_group_item(self):
        '''
        Test creating a product group item.
        '''
        product = Product.objects.create(
            name='Product 1',
            description='Description 1',
            release_date=datetime.date(2020, 1, 1),
            price=10.00,
            stock=10,
        )
        group = ProductGroup.objects.create(
            name='Group 1',
        )
        group_item = ProductGroupItem.objects.create(
            product=product,
            group=group,
        )
        self.assertEqual(group_item.product, product)
        self.assertEqual(group_item.group, group)
