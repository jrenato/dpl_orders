'''
Views for the suppliers app
'''
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Supplier
from .forms import SupplierForm


class SupplierListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Supplier model
    '''
    model = Supplier
    context_object_name = 'suppliers'
    permission_required = 'suppliers.view_supplier'


class SupplierDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Supplier model
    '''
    model = Supplier
    context_object_name = 'supplier'
    permission_required = 'suppliers.view_supplier'


class SupplierCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Supplier model
    '''
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:list')
    permission_required = 'suppliers.add_supplier'


class SupplierUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Supplier model
    '''
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:list')
    permission_required = 'suppliers.change_supplier'


class SupplierDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Supplier model
    '''
    model = Supplier
    success_url = reverse_lazy('suppliers:list')
    permission_required = 'suppliers.delete_supplier'
