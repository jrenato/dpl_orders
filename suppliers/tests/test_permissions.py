'''
This file contains tests for the permissions of the suppliers app.
'''
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from suppliers.models import Supplier



class SuppliersPermissionsTest(TestCase):
    '''
    Tests for the Customers permission
    '''
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.supplier = Supplier.objects.create(
            name='Test Supplier',
            slug='test-supplier',
            cnpj='12345678901234',
        )

    def test_redirect_if_not_logged_in(self):
        '''
        Test if the user is redirected to the login page if not logged in
        '''
        response = self.client.get(reverse('suppliers:list'))
        self.assertRedirects(response, '/accounts/login/?next=/suppliers/')

    def test_logged_in_user_no_permission_to_view_list(self):
        '''
        Test if the user has no permission to view the list of suppliers
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:list'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_list(self):
        '''
        Test if the user has permission to view the list of suppliers
        '''
        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:list'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_view_detail(self):
        '''
        Test if the user has no permission to view the detail of a supplier
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:detail', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_detail(self):
        '''
        Test if the user has permission to view the detail of a supplier
        '''
        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_create(self):
        '''
        Test if the user has no permission to create a supplier
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:create'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_create(self):
        '''
        Test if the user has permission to create a supplier
        '''
        permission = Permission.objects.get(codename='add_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:create'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_update(self):
        '''
        Test if the user has no permission to update a supplier
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:update', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_update(self):
        '''
        Test if the user has permission to update a supplier
        '''
        permission = Permission.objects.get(codename='change_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:update', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_delete(self):
        '''
        Test if the user has no permission to delete a supplier
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:delete', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_delete(self):
        '''
        Test if the user has permission to delete a supplier
        '''
        permission = Permission.objects.get(codename='delete_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:delete', args=[self.supplier.id]))
        self.assertEqual(response.status_code, 200)
