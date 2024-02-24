'''
This file contains the tests for the Order model.
'''
from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from orders.models import Order, ORDER_STATUS_CHOICES
from customers.models import Customer


class OrderTest(TestCase):
    '''
    Test case for the Order model
    '''
    def test_create_order(self):
        '''
        Test the creation of an order
        '''
        customer = Customer.objects.create(name="John Doe")
        order = Order.objects.create(customer=customer)
        self.assertEqual(order.status, ORDER_STATUS_CHOICES[0][0])  # Default status
        self.assertEqual(str(order), f"{customer} - {order.created}")

    def test_order_status_choices(self):
        '''
        Test the order status choices
        '''
        choices = dict(ORDER_STATUS_CHOICES)
        self.assertEqual(choices["PE"], _("Pending"))
        self.assertEqual(choices["FI"], _("Finished"))
