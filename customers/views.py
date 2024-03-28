'''
Views for the customers app.
'''
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.forms.models import inlineformset_factory

from crispy_forms.layout import Layout, Submit

from .models import Customer, CustomerAddress, CustomerPhone
from .forms import CustomerForm, CustomerAddressForm, CustomerPhoneForm, \
    CustomerFormSetHelper, CustomerAddressFormSetHelper, CustomerPhoneFormSetHelper


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


# Function Based View to update the customer,
# using inlineformset for the CustomerAddress and CustomerPhone models
def update_customer(request, slug):
    customer = Customer.objects.get(slug=slug)
    CustomerAddressFormSet = inlineformset_factory(Customer, CustomerAddress, form=CustomerAddressForm, extra=1, can_delete=False)
    CustomerPhoneFormSet = inlineformset_factory(Customer, CustomerPhone, form=CustomerPhoneForm, extra=1, can_delete=True)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=customer)
        customer_address_formset = CustomerAddressFormSet(request.POST, instance=customer)
        customer_phone_formset = CustomerPhoneFormSet(request.POST, instance=customer)
        if customer_form.is_valid() and customer_address_formset.is_valid() and customer_phone_formset.is_valid():
            customer_form.save()
            customer_address_formset.save()
            customer_phone_formset.save()
            return redirect('customers:detail', slug=customer.slug)
    else:
        customer_form = CustomerForm(instance=customer)
        customer_address_formset = CustomerAddressFormSet(instance=customer)
        customer_phone_formset = CustomerPhoneFormSet(instance=customer)
    return render(request, 'customers/customer_formset.html', {
        'customer_form': customer_form,
        'customer_address_formset': customer_address_formset,
        'customer_phone_formset': customer_phone_formset,
    })


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Customer model
    '''
    model = Customer
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'
