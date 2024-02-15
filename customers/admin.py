'''
Admin for Customers app
'''
from django.contrib import admin

from .models import Customer, CustomerAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Admin for the Customer model
    '''
    list_display = ('name', 'short_name', 'email', 'cnpj', 'cpf',)
    search_fields = ('name', 'short_name', 'email', 'cnpj', 'cpf', 'phone',)
    #list_filter = ('created', 'modified')
    list_per_page = 20


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    '''
    Admin for the CustomerAddress model
    '''
    list_display = ('customer', 'street', 'number', 'city', 'state', 'zip_code',)
    search_fields = ('customer__name', 'street', 'city', 'state', 'zip_code',)
    list_filter = ('state',)
    list_per_page = 20
