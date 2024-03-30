'''
Views for the customers app.
'''
from django.urls import reverse_lazy
from django.db.models import Count, Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin

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


# Function Based View to update the customer,
# using inlineformset for the CustomerAddress and CustomerPhone models
class UpdateCustomerView(FormView):
    template_name = 'customers/customer_formset.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers:detail')

    def get_object(self):
        """
        Retrieves a `Customer` object based on the provided `slug`.

        Returns:
            Customer: The `Customer` object matching the provided `slug`.
        """
        slug = self.kwargs.get('slug')
        return Customer.objects.get(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        context['customer_address_formset'] = CustomerAddressFormSet(instance=customer)
        context['customer_phone_formset'] = CustomerPhoneFormSet(instance=customer)
        return context

    def form_valid(self, form):
        customer = self.get_object()
        customer_form = form.save(commit=False)
        customer_form.save()
        customer_address_formset = self.get_context_data()['customer_address_formset']
        customer_phone_formset = self.get_context_data()['customer_phone_formset']
        if customer_address_formset.is_valid() and customer_phone_formset.is_valid():
            customer_address_formset.save()
            customer_phone_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Customer model
    '''
    model = Customer
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'
