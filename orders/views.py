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

    # TODO: Finish this method
    def delete(self, request, *args, **kwargs):
        # Should mark the order as canceled instead of deleting it
        # Also, should mark the order items as canceled

        # order = self.get_object()
        # order.canceled = timezone.now()
        # canceled_status = [status[0] for status in ORDER_STATUS_CHOICES
        #                    if status[1] == 'Canceled'][0]
        # order.status = canceled_status
        # order.save()

        # item_finished_status = [status[0] for status in ORDER_ITEM_STATUS_CHOICES
        #                         if status[1] == 'Finished'][0]
        # item_cancel_status = [status[0] for status in ORDER_ITEM_STATUS_CHOICES
        #                         if status[1] == 'Canceled'][0]

        # # Mark all the order items as canceled, except the ones that are already finished
        # for order_item in order.order_items.exclude(status=item_finished_status):
        #     order_item.canceled = timezone.now()
        #     order_item.status = item_cancel_status
        #     order_item.save()

        # Don't call the super method, just redirect to the success url
        return HttpResponseRedirect(self.get_success_url())
