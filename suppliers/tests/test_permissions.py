'''
This file contains tests for the permissions of the suppliers app.
'''
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _

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

    # Template tests

    ## Home link
    def test_user_without_permission_to_view_cant_see_home_link(self):
        '''
        Test if the user without permission to view a supplier can't see the home link
        '''
        self.client.login(username='testuser', password='testpass123')

        response = self.client.get(reverse('home'))
        self.assertNotContains(response, _('Suppliers'))

    def test_user_with_permission_to_view_can_see_home_link(self):
        '''
        Test if the user with permission to view a supplier can see the home link
        '''
        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertContains(response, _('Suppliers'))

    ## Add button
    def test_user_without_permission_to_create_cant_see_add_button(self):
        '''
        Test if the user without permission to create a supplier can't see the add button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('suppliers:list'))
        self.assertNotContains(response, _('Add'))

    def test_user_with_permission_to_create_can_see_add_button(self):
        '''
        Test if the user with permission to create a supplier can see the add button
        '''
        permission_to_view = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission_to_view)
        permission_to_add = Permission.objects.get(codename='add_supplier')
        self.user.user_permissions.add(permission_to_add)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:list'))
        self.assertContains(response, _('Add'))

    ## Edit button
    def test_user_without_permission_to_update_cant_see_edit_button(self):
        '''
        Test if the user without permission to update a supplier can't see the edit button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('suppliers:detail', args=[self.supplier.id]))
        self.assertNotContains(response, _('Edit'))

    def test_user_with_permission_to_update_can_see_edit_button(self):
        '''
        Test if the user with permission to update a supplier can see the edit button
        '''
        permission_to_view = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission_to_view)
        permission_to_update = Permission.objects.get(codename='change_supplier')
        self.user.user_permissions.add(permission_to_update)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:detail', args=[self.supplier.id]))
        self.assertContains(response, _('Edit'))

    ## Delete button
    def test_user_without_permission_to_delete_cant_see_delete_button(self):
        '''
        Test if the user without permission to delete a supplier can't see the delete button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('suppliers:detail', args=[self.supplier.id]))
        self.assertNotContains(response, _('Delete'))

    def test_user_with_permission_to_delete_can_see_delete_button(self):
        '''
        Test if the user with permission to delete a supplier can see the delete button
        '''
        permission_to_view = Permission.objects.get(codename='view_supplier')
        self.user.user_permissions.add(permission_to_view)
        permission_to_delete = Permission.objects.get(codename='delete_supplier')
        self.user.user_permissions.add(permission_to_delete)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('suppliers:detail', args=[self.supplier.id]))
        self.assertContains(response, _('Delete'))
