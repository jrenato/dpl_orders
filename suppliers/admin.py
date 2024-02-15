'''
Admin for Suppliers app
'''
from django.contrib import admin
from .models import Supplier, SupplierAddress


class SupplierAddressInline(admin.StackedInline):
    '''
    SupplierAddressInline class
    '''
    model = SupplierAddress
    readonly_fields = ('created', 'modified',)
    extra = 1


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    '''
    Admin for the Supplier model
    '''
    list_display = ('name', 'short_name', 'contact_person', 'email', 'phone_number')
    search_fields = ('name', 'short_name', 'contact_person', 'email', 'phone_number')
    readonly_fields = ('created', 'modified',)
    inlines = [SupplierAddressInline]
