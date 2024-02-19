'''
Admin for the Product Groups
'''
from django.contrib import admin

from .models import ProductGroup


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
