'''
Views for the orders app.
'''
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Order, ORDER_STATUS_CHOICES, OrderItem, ORDER_ITEM_STATUS_CHOICES
from .forms import OrderForm


class OrderListView(PermissionRequiredMixin, ListView):
    '''
    List view for Order model
    '''
    model = Order
    context_object_name = 'orders'
    paginate_by = 20
    permission_required = 'orders.view_order'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset\
        .prefetch_related('customer', 'product_group', 'order_items', 'order_items__product')\
        .annotate(
            total_quantity=Sum('order_items__quantity'),
            total_value=Sum('order_items__subtotal')
        )\
        .order_by('customer__name')

        return queryset


class OrderDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for Order model
    '''
    model = Order
    context_object_name = 'order'
    permission_required = 'orders.view_order'

    def get_queryset(self):
        return super().get_queryset()\
        .prefetch_related('customer', 'product_group', 'order_items', 'order_items__product')\
        .annotate(
            total_quantity=Sum('order_items__quantity'),
            total_value=Sum('order_items__subtotal')
        )


class OrderCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for Order model
    '''
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:list')
    permission_required = 'orders.add_order'


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for Order model
    '''
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:list')
    permission_required = 'orders.change_order'


class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for Order model
    '''
    model = Order
    success_url = reverse_lazy('orders:list')
    permission_required = 'orders.delete_order'
