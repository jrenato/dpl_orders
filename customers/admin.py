'''
Admin for Customers app
'''
from django.contrib import admin

from .models import Customer, CustomerAddress


class CustomerAddressInline(admin.StackedInline):
    '''
    CustomerAddressInline class
    '''
    model = CustomerAddress
    readonly_fields = ('created', 'updated',)
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''
    Admin for the Customer model
    '''
    list_display = ('short_name', 'name', 'cnpj', 'cpf',)
    search_fields = ('name', 'short_name', 'email', 'cnpj', 'cpf',)
    #list_filter = ('created', 'updated')
    list_per_page = 20
    readonly_fields = ('created', 'updated',)
    inlines = [CustomerAddressInline]
