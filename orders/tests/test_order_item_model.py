'''
This file contains the tests for the OrderItem model.
'''
import datetime

from django.test import TestCase

from orders.models import Order, OrderItem, OrderItemHistory
from customers.models import Customer
from products.models import Product


class OrderItemTest(TestCase):
    '''
    Test case for the OrderItem model
    '''
    def test_create_order_item(self):
        '''
        Test the creation of an order item
        '''
        product = Product.objects.create(
            name="Product 1", price=10.00, release_date=datetime.date.today()
        )
        order = Order.objects.create(customer=Customer.objects.create(name="John Doe"))
        order_item = OrderItem.objects.create(order=order, product=product, quantity=2)
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(str(order_item), f"{product} - 2")

    def test_save_without_quantity_change(self):
        '''
        Test the save method without a quantity change
        '''
        product = Product.objects.create(
            name="Product 1", price=10.00, release_date=datetime.date.today()
        )
        order = Order.objects.create(customer=Customer.objects.create(name="John Doe"))
        order_item = OrderItem.objects.create(order=order, product=product, quantity=2)
        order_item.save()
        history = OrderItemHistory.objects.filter(order_item=order_item)
        self.assertTrue(history.exists())
        history_item = history.first()
        self.assertEqual(history_item.quantity, 2)

    def test_save_with_quantity_change(self):
        '''
        Test the save method with a quantity change
        '''
        product = Product.objects.create(
            name="Product 1", price=10.00, release_date=datetime.date.today()
        )
        order = Order.objects.create(customer=Customer.objects.create(name="John Doe"))
        order_item = OrderItem.objects.create(order=order, product=product, quantity=2)
        order_item.quantity = 3
        order_item.save()
        history = OrderItemHistory.objects.filter(order_item=order_item).order_by("-created")
        self.assertTrue(history.exists())
        history_item = history.first()
        self.assertEqual(history_item.quantity, 3)
        last_history = history.last()
        self.assertEqual(last_history.quantity, 2)
