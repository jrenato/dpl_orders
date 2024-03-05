'''
Views for the orders app.
'''
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Order
from .forms import OrderForm


class OrderListView(PermissionRequiredMixin, ListView):
    '''
    List view for Order model
    '''
    model = Order
    context_object_name = 'orders'
    permission_required = 'orders.view_order'

    def get_queryset(self):
        return super().get_queryset().annotate(
            total_quantity=Sum('order_items__quantity'),
            total_value=Sum('order_items__subtotal')
        )


class OrderDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for Order model
    '''
    model = Order
    context_object_name = 'order'
    permission_required = 'orders.view_order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = self.object.order_items.all()
        return context

    def get_queryset(self):
        return super().get_queryset().annotate(
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
