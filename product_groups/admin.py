'''
Admin for the Product Groups
'''
from django.contrib import admin

from .models import ProductGroup, ProductGroupStatus


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    '''
    Admin for the Product Group
    '''
    list_display = ['name', 'status', 'customer_limit_date', 'supplier_limit_date',]
    search_fields = ['name', 'status',]
    list_filter = ['status', 'customer_limit_date', 'supplier_limit_date',]
    date_hierarchy = 'supplier_limit_date'
    readonly_fields = ['created', 'modified']


@admin.register(ProductGroupStatus)
class ProductGroupStatusAdmin(admin.ModelAdmin):
    '''
    Admin for the Product Group Status
    '''
    list_display = ['name',]
    search_fields = ['name']
    readonly_fields = ['created', 'modified']
