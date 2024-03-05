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
    def setUp(self):
        '''
        Set up the test case
        '''
        self.customer = Customer.objects.create(name="John Doe")
        self.order = Order.objects.create(customer=self.customer)

    def test_create_order(self):
        '''
        Test the creation of an order
        '''
        self.assertEqual(self.order.get_status_display(), _("Pending"))
        self.assertEqual(str(self.order), f"{self.customer} - {self.order.created}")

    def test_order_status_choices(self):
        '''
        Test the order status choices
        '''
        choices = dict(ORDER_STATUS_CHOICES)
        self.assertEqual(choices["PE"], _("Pending"))
        self.assertEqual(choices["FI"], _("Finished"))

    # def test_order_delete_should_not_delete_but_mark_as_canceled(self):
    #     '''
    #     Test the delete method of the Order model
    #     '''
    #     order_id = self.order.id
    #     self.order.delete()

    #     # Assert the order is not deleted
    #     self.assertTrue(Order.objects.filter(id=order_id).exists())

    #     # If the order is not deleted, it should be marked as canceled
    #     self.order.refresh_from_db()
    #     self.assertIsNotNone(self.order.canceled)
    #     self.assertEqual(self.order.status, "CA")
    #     self.assertEqual(self.order.get_status_display(), _("Canceled"))
