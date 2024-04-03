'''
Views for the customers app.
'''
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction

from crispy_forms.layout import Layout, Submit

from .models import Customer, CustomerAddress, CustomerPhone
from .forms import CustomerForm, CustomerAddressForm, CustomerPhoneForm, \
    CustomerAddressFormSet, CustomerPhoneFormSet


class CustomerListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Customer model
    '''
    model = Customer
    context_object_name = 'customers'
    permission_required = 'customers.view_customer'

    def get_queryset(self):
        # Prefetch the count of orders for each customer as order_count
        return Customer.objects\
            .prefetch_related('orders', 'orders__order_items')\
            .annotate(
                order_count=Count('orders', distinct=True),
                ordered_total=Sum('orders__order_items__quantity')
            )


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Customer model
    '''
    model = Customer
    context_object_name = 'customer'
    permission_required = 'customers.view_customer'

    # def get_queryset(self):
    #     return Customer.objects\
    #         .prefetch_related('orders',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pending_orders'] = self.object.orders\
            .filter(status='PE')\
            .annotate(
                total_quantity=Sum('order_items__quantity'),
                total_value=Sum('order_items__subtotal')
            )\
            .order_by('-created')

        return context


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


class CreateCustomerView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Customer model
    '''
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_formset.html'
    permission_required = 'customers.add_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['addresses'] = CustomerAddressFormSet(self.request.POST)
        else:
            context['addresses'] = CustomerAddressFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context['addresses']
        with transaction.atomic():
            if addresses.is_valid():
                customer = form.save()
                addresses.instance = customer
                addresses.save()
        return super().form_valid(form)


class UpdateCustomerView(PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_formset.html'
    permission_required = 'customers.change_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['addresses'] = CustomerAddressFormSet(self.request.POST, instance=self.object)
        else:
            context['addresses'] = CustomerAddressFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context['addresses']
        with transaction.atomic():
            if addresses.is_valid():
                addresses.instance = self.object
                addresses.save()
        return super().form_valid(form)


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Customer model
    '''
    model = Customer
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'
