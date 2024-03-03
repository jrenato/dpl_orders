'''
This file contains tests for the permissions of the products app.
'''
import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.translation import gettext as _

from products.models import Product


class ProductsPermissionsTest(TestCase):
    '''
    Tests for the Products permission
    '''
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.product = Product.objects.create(
            name='Test Product',
            sku='12345678901234',
            release_date=datetime.date.today(),
        )

    def test_redirect_if_not_logged_in(self):
        '''
        Test if the user is redirected to the login page if not logged in
        '''
        response = self.client.get(reverse('products:list'))
        self.assertRedirects(response, '/accounts/login/?next=/products/')

    def test_logged_in_user_no_permission_to_view_list(self):
        '''
        Test if the user has no permission to view the list of products
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_list(self):
        '''
        Test if the user has permission to view the list of products
        '''
        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:list'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_view_detail(self):
        '''
        Test if the user has no permission to view the detail of a product
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_view_detail(self):
        '''
        Test if the user has permission to view the detail of a product
        '''
        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_create(self):
        '''
        Test if the user has no permission to create a product
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:create'))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_create(self):
        '''
        Test if the user has permission to create a product
        '''
        permission = Permission.objects.get(codename='add_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:create'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_update(self):
        '''
        Test if the user has no permission to update a product
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:update', args=[self.product.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_update(self):
        '''
        Test if the user has permission to update a product
        '''
        permission = Permission.objects.get(codename='change_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:update', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_has_no_permission_to_delete(self):
        '''
        Test if the user has no permission to delete a product
        '''
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 403)

    def test_logged_in_user_has_permission_to_delete(self):
        '''
        Test if the user has permission to delete a product
        '''
        permission = Permission.objects.get(codename='delete_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:delete', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    # Template tests

    ## Home link
    def test_user_without_permission_to_view_cant_see_home_link(self):
        '''
        Test if the user without permission to view a product can't see the home link
        '''
        self.client.login(username='testuser', password='testpass123')

        response = self.client.get(reverse('home'))
        self.assertNotContains(response, _('Products'))

    def test_user_with_permission_to_view_can_see_home_link(self):
        '''
        Test if the user with permission to view a product can see the home link
        '''
        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('home'))
        self.assertContains(response, _('Products'))

    ## Add button
    def test_user_without_permission_to_create_cant_see_add_button(self):
        '''
        Test if the user without permission to create a product can't see the add button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('products:list'))
        self.assertNotContains(response, _('Add'))

    def test_user_with_permission_to_create_can_see_add_button(self):
        '''
        Test if the user with permission to create a product can see the add button
        '''
        permission_to_view = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission_to_view)
        permission_to_add = Permission.objects.get(codename='add_product')
        self.user.user_permissions.add(permission_to_add)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:list'))
        self.assertContains(response, _('Add'))

    ## Edit button
    def test_user_without_permission_to_update_cant_see_edit_button(self):
        '''
        Test if the user without permission to update a product can't see the edit button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('products:detail', args=[self.product.id]))
        self.assertNotContains(response, _('Edit'))

    def test_user_with_permission_to_update_can_see_edit_button(self):
        '''
        Test if the user with permission to update a product can see the edit button
        '''
        permission_to_view = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission_to_view)
        permission_to_update = Permission.objects.get(codename='change_product')
        self.user.user_permissions.add(permission_to_update)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:detail', args=[self.product.id]))
        self.assertContains(response, _('Edit'))

    ## Delete button
    def test_user_without_permission_to_delete_cant_see_delete_button(self):
        '''
        Test if the user without permission to delete a product can't see the delete button
        '''
        self.client.login(username='testuser', password='testpass123')

        permission = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission)

        response = self.client.get(reverse('products:detail', args=[self.product.id]))
        self.assertNotContains(response, _('Delete'))

    def test_user_with_permission_to_delete_can_see_delete_button(self):
        '''
        Test if the user with permission to delete a product can see the delete button
        '''
        permission_to_view = Permission.objects.get(codename='view_product')
        self.user.user_permissions.add(permission_to_view)
        permission_to_delete = Permission.objects.get(codename='delete_product')
        self.user.user_permissions.add(permission_to_delete)

        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('products:detail', args=[self.product.id]))
        self.assertContains(response, _('Delete'))
