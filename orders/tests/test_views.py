'''
This file contains the test cases for the views of the orders app.
'''
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.utils import timezone

from customers.models import Customer
from suppliers.models import Supplier
from products.models import Product
from orders.models import Order, OrderItem


class OrderViewsTestCase(TestCase):
    '''
    Test case for the views of the orders app
    '''
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.customer = Customer.objects.create(name='Test Customer')
        self.supplier = Supplier.objects.create(name='Test Supplier')
        self.product1 = Product.objects.create(
            name='Test Product',
            supplier=self.supplier,
            sku='9876543210',
            release_date=timezone.now(),
            price=100.00,
            stock=10,
        )
        self.product2 = Product.objects.create(
            name='Test Product 2',
            supplier=self.supplier,
            sku='1234567890',
            release_date=timezone.now(),
            price=200.00,
            stock=20,
        )

    def test_order_list_view_with_no_orders(self):
        '''
        Test the order list view with no orders
        '''
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('orders:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')
        self.assertContains(response, _('No orders available'))
        self.assertQuerysetEqual(response.context['orders'], [])

    def test_order_list_view_with_orders(self):
        '''
        Test the order list view with orders
        '''
        self.client.login(username='testuser', password='testpassword')
        order = Order.objects.create(
            customer=self.customer,
        )
        response = self.client.get(reverse('orders:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')
        self.assertContains(response, order.customer.username)
        self.assertContains(response, order.status)
        self.assertContains(response, order.total_amount)
        self.assertQuerysetEqual(
            response.context['orders'], ['<Order: Test Customer - {}>'.format(order.created)]
        )

    # def test_order_detail_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.get(reverse('orders:detail', args=[self.order.pk]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'orders/order_detail.html')
    #     self.assertContains(response, self.order.customer.username)
    #     self.assertContains(response, self.order.status)
    #     self.assertContains(response, self.order.total_amount)
    #     self.assertContains(response, self.order_item.product_name)
    #     self.assertContains(response, self.order_item.quantity)
    #     self.assertContains(response, self.order_item.price)

    # def test_order_create_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.post(reverse('orders:create'), {
    #         'customer': self.user.pk,
    #         'status': 'Pending',
    #         'total_amount': 100.00,
    #         'created_at': timezone.now()
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('orders:list'))

    # def test_order_update_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.post(reverse('orders:update', args=[self.order.pk]), {
    #         'customer': self.user.pk,
    #         'status': 'Completed',
    #         'total_amount': 200.00,
    #         'created_at': timezone.now()
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('orders:list'))

    # def test_order_delete_view(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.post(reverse('orders:delete', args=[self.order.pk]))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('orders:list'))
    #     self.order.refresh_from_db()
    #     self.assertEqual(self.order.status, 'Canceled')
    #     self.order_item.refresh_from_db()
    #     self.assertEqual(self.order_item.status, 'Canceled')
