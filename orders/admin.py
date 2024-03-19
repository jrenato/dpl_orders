'''
This file is used to register the models in the admin panel.
'''
from django.contrib import admin

from .models import Order, OrderItem, OrderStatusHistory, OrderItemHistory


class OrderItemInline(admin.TabularInline):
    '''
    Inline for Order Item
    '''
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


class OrderStatusHistoryInline(admin.TabularInline):
    '''
    Inline for Order Status History
    '''
    model = OrderStatusHistory
    extra = 0


class OrderItemHistoryInline(admin.TabularInline):
    '''
    Inline for Order Item History
    '''
    model = OrderItemHistory
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''
    Admin View for Order
    '''
    list_display = ['customer', 'status', 'created', 'updated']
    list_filter = ['status', 'created']
    search_fields = ['customer__name',]
    readonly_fields = ['created', 'updated']
    inlines = [OrderItemInline, OrderStatusHistoryInline]

    autocomplete_fields = ['customer', 'product_group']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''
    Admin View for Order Item
    '''
    list_display = ['order', 'product', 'price', 'quantity', 'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemHistoryInline]
