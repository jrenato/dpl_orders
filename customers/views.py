'''
Views for the customers app.
'''
from django.urls import reverse_lazy
from django.db.models import Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Customer
from .forms import CustomerForm


class CustomerListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Customer model
    '''
    model = Customer
    context_object_name = 'customers'
    permission_required = 'customers.view_customer'

    def get_queryset(self):
        # Prefetch the count of orders for each customer as order_count
        return Customer.objects.prefetch_related('orders').annotate(
            order_count=Count('orders')
        )


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Customer model
    '''
    model = Customer
    context_object_name = 'customer'
    permission_required = 'customers.view_customer'


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Customer model
    '''
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.add_customer'


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Customer model
    '''
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.change_customer'


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Customer model
    '''
    model = Customer
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'
