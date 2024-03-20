'''
Views for the orders app.
'''
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Order, OrderItem
from .forms import OrderCreateForm, OrderUpdateForm, OrderItemCreateForm, OrderItemUpdateForm


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
            total_quantity=Sum('order_items__quantity', default=0),
            total_value=Sum('order_items__subtotal', default=0)
        )\
        .order_by('customer__name')

        return queryset


class OrderDetailView(PermissionRequiredMixin, MultipleObjectMixin, DetailView):
    '''
    Detail view for Order model
    '''
    model = Order
    #context_object_name = 'order'
    paginate_by = 20
    permission_required = 'orders.view_order'

    def get_queryset(self):
        return super().get_queryset()\
        .prefetch_related('customer', 'product_group', 'order_items', 'order_items__product')\
        .annotate(
            total_quantity=Sum('order_items__quantity'),
            total_value=Sum('order_items__subtotal')
        )

    def get_context_data(self, **kwargs):
        object_list = self.get_object().order_items\
            .select_related('product', 'product__category', 'product__supplier')\
            .order_by('product__name')
        context = super(OrderDetailView, self)\
            .get_context_data(object_list=object_list, **kwargs)
        return context

class OrderCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for Order model
    '''
    model = Order
    form_class = OrderCreateForm
    permission_required = 'orders.add_order'

    def get_success_url(self):
        return reverse_lazy('orders:detail', kwargs={'pk': self.object.pk})


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for Order model
    '''
    model = Order
    form_class = OrderUpdateForm
    success_url = reverse_lazy('orders:list')
    permission_required = 'orders.change_order'


class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for Order model
    '''
    model = Order
    success_url = reverse_lazy('orders:list')
    permission_required = 'orders.delete_order'


### Order Item views ###


class OrderItemCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for Order Item
    '''
    model = OrderItem
    form_class = OrderItemCreateForm
    permission_required = 'orders.add_orderitem'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'order': self.get_order_object()}
        return kwargs

    def get_order_object(self):
        '''
        Get order object
        '''
        order_pk = self.kwargs.get('pk')
        return Order.objects.get(pk=order_pk)

    def get_success_url(self):
        return reverse_lazy('orders:detail', kwargs={'pk': self.object.order.pk})


class OrderItemUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for Order Item
    '''
    model = OrderItem
    form_class = OrderItemUpdateForm
    permission_required = 'orders.change_orderitem'

    def get_success_url(self):
        return reverse_lazy('orders:detail', kwargs={'pk': self.object.order.pk})


class OrderItemDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for Order Item
    '''
    model = OrderItem
    permission_required = 'orders.delete_orderitem'

    def get_success_url(self):
        return reverse_lazy('orders:detail', kwargs={'pk': self.object.order.pk})
