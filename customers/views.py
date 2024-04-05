'''
Views for the customers app.
'''
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction

from .models import Customer, CustomerPhone
from .forms import CustomerForm, CustomerAddressFormSet, CustomerAddressFormSetHelper, \
    CustomerPhoneForm


class CustomerListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Customer model
    '''
    model = Customer
    context_object_name = 'customers'
    permission_required = 'customers.view_customer'

    def get_queryset(self):
        return Customer.objects\
            .prefetch_related('orders', 'orders__order_items')\
            .annotate(
                order_count=Count('orders', distinct=True),
                ordered_total=Sum('orders__order_items__quantity', default=0)
            )


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Customer model
    '''
    model = Customer
    context_object_name = 'customer'
    permission_required = 'customers.view_customer'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['address_formset'] = CustomerAddressFormSet(self.request.POST)
            context['address_formset_helper'] = CustomerAddressFormSetHelper()
        else:
            context['address_formset'] = CustomerAddressFormSet()
            context['address_formset_helper'] = CustomerAddressFormSetHelper()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_formset = context['address_formset']
        with transaction.atomic():
            if address_formset.is_valid():
                customer = form.save()
                address_formset.instance = customer
                address_formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'slug': self.object.slug})


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Customer model
    '''
    model = Customer
    form_class = CustomerForm
    permission_required = 'customers.change_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['address_formset'] = CustomerAddressFormSet(
                self.request.POST, instance=self.object)
            context['address_formset_helper'] = CustomerAddressFormSetHelper()
        else:
            context['address_formset'] = CustomerAddressFormSet(instance=self.object)
            context['address_formset_helper'] = CustomerAddressFormSetHelper()

        return context

    def form_valid(self, form):
        context = self.get_context_data()

        address_formset = context['address_formset']
        with transaction.atomic():
            if address_formset.is_valid():
                address_formset.instance = self.object
                address_formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'slug': self.object.slug})


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Customer model
    '''
    model = Customer
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'


### Phone Views ###


class CustomerPhoneCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the CustomerPhone model
    '''
    model = CustomerPhone
    form_class = CustomerPhoneForm
    permission_required = 'customers.add_customerphone'

    def get_initial(self):
        customer = Customer.objects.get(slug=self.kwargs['slug'])
        return {
            'customer': customer
        }

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'slug': self.object.customer.slug})


class CustomerPhoneUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the CustomerPhone model
    '''
    model = CustomerPhone
    form_class = CustomerPhoneForm
    permission_required = 'customers.change_customerphone'

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'slug': self.object.customer.slug})


class CustomerPhoneDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the CustomerPhone model
    '''
    model = CustomerPhone
    permission_required = 'customers.delete_customerphone'

    def get_success_url(self):
        return reverse_lazy('customers:detail', kwargs={'slug': self.object.customer.slug})
