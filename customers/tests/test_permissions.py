'''
This file contains tests for the permissions of the customers app.
'''
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _

from customers.models import Customer



class CustomersPermissionsTest(TestCase):
    '''
    Tests for the Customers permission
    '''
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.customer = Customer.objects.create(
            name='Test Customer',
            slug='test-customer',
            cnpj='12345678901234',
        )

    def test_redirect_if_not_logged_in(self):
        '''
        Test if the user is redirected to the login page if not logged in
        '''
        response = self.client.get(reverse('customers:list'))
        self.assertRedirects(response, '/accounts/login/?next=/customers/')

    def test_logged_in_user_no_permission_to_view_list(self):
        '''
        Test if the user has no permission to view the list of customers
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:list'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_list(self):
        '''
        Test if the user has permission to view the list of customers
        '''
        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:list'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_view_detail(self):
        '''
        Test if the user has no permission to view the detail of a customer
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_detail(self):
        '''
        Test if the user has permission to view the detail of a customer
        '''
        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_create(self):
        '''
        Test if the user has no permission to create a customer
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:create'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_create(self):
        '''
        Test if the user has permission to create a customer
        '''
        permission = Permission.objects.get(codename='add_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:create'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_update(self):
        '''
        Test if the user has no permission to update a customer
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:update', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_update(self):
        '''
        Test if the user has permission to update a customer
        '''
        permission = Permission.objects.get(codename='change_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:update', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_delete(self):
        '''
        Test if the user has no permission to delete a customer
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:delete', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_delete(self):
        '''
        Test if the user has permission to delete a customer
        '''
        permission = Permission.objects.get(codename='delete_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:delete', args=[self.customer.slug]))
        self.assertEqual(response.status_code, 200)

    # Template tests

    ## Home link
    def test_user_without_permission_to_view_cant_see_home_link(self):
        '''
        Test if the user without permission to view a customer can't see the home link
        '''
        self.client.login(username='testuser', password='testpass123')

        response = self.client.get(reverse('home'))
        self.assertNotContains(response, _('Customers'))

    def test_user_with_permission_to_view_can_see_home_link(self):
        '''
        Test if the user with permission to view a customer can see the home link
        '''
        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertContains(response, _('Customers'))

    ## Add button
    def test_user_without_permission_to_create_cant_see_add_button(self):
        '''
        Test if the user without permission to create a customer can't see the add button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('customers:list'))
        self.assertNotContains(response, _('Add'))

    def test_user_with_permission_to_create_can_see_add_button(self):
        '''
        Test if the user with permission to create a customer can see the add button
        '''
        permission_to_view = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission_to_view)
        permission_to_add = Permission.objects.get(codename='add_customer')
        self.user.user_permissions.add(permission_to_add)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:list'))
        self.assertContains(response, _('Add'))

    ## Edit button
    def test_user_without_permission_to_update_cant_see_edit_button(self):
        '''
        Test if the user without permission to update a customer can't see the edit button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertNotContains(response, _('Edit'))

    def test_user_with_permission_to_update_can_see_edit_button(self):
        '''
        Test if the user with permission to update a customer can see the edit button
        '''
        permission_to_view = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission_to_view)
        permission_to_update = Permission.objects.get(codename='change_customer')
        self.user.user_permissions.add(permission_to_update)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertContains(response, _('Edit'))

    ## Delete button
    def test_user_without_permission_to_delete_cant_see_delete_button(self):
        '''
        Test if the user without permission to delete a customer can't see the delete button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertNotContains(response, _('Delete'))

    def test_user_with_permission_to_delete_can_see_delete_button(self):
        '''
        Test if the user with permission to delete a customer can see the delete button
        '''
        permission_to_view = Permission.objects.get(codename='view_customer')
        self.user.user_permissions.add(permission_to_view)
        permission_to_delete = Permission.objects.get(codename='delete_customer')
        self.user.user_permissions.add(permission_to_delete)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('customers:detail', args=[self.customer.slug]))
        self.assertContains(response, _('Delete'))
