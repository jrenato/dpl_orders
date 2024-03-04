'''
This file contains the tests for the OrderItem model.
'''
import datetime

from django.test import TestCase

from orders.models import Order, OrderItem, OrderItemHistory
from customers.models import Customer
from products.models import Product
from suppliers.models import Supplier


class OrderItemTest(TestCase):
    '''
    Test case for the OrderItem model
    '''
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Supplier 1")
        self.product = Product.objects.create(
            name="Product 1", price=10.00, supplier=self.supplier,
            release_date=datetime.date.today(),
        )
        self.customer = Customer.objects.create(name="John Doe")

    def test_create_order_item(self):
        '''
        Test the creation of an order item
        '''
        order = Order.objects.create(customer=self.customer)
        order_item = OrderItem.objects.create(order=order, product=self.product, quantity=2)

        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.price, self.product.price)
        self.assertEqual(order_item.subtotal, self.product.price * 2)
        self.assertEqual(str(order_item), f"{self.product} - 2")

        # History should be created automatically
        history_item = OrderItemHistory.objects.get(order_item=order_item)
        self.assertEqual(history_item.quantity, 2)


    def test_save_with_quantity_change(self):
        '''
        Test the save method with a quantity change
        '''
        order = Order.objects.create(customer=self.customer)
        order_item = OrderItem.objects.create(order=order, product=self.product, quantity=2)

        # Assert the subtotal is correct
        self.assertEqual(order_item.subtotal, self.product.price * 2)

        # Change the quantity
        order_item.quantity = 3
        order_item.save()

        # Refresh the order item
        order_item.refresh_from_db()

        # Assert the subtotal is correct
        self.assertEqual(order_item.subtotal, self.product.price * 3)

        # Now there should be two history items
        history = OrderItemHistory.objects.filter(order_item=order_item).order_by("-created")
        self.assertTrue(history.exists())
        
        # The first history item should have quantity 3
        history_item = history.first()
        self.assertEqual(history_item.quantity, 3)

        # The last history item should have quantity 2
        last_history = history.last()
        self.assertEqual(last_history.quantity, 2)
