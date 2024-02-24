'''
Views for the suppliers app
'''
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    '''
    List view for the Supplier model
    '''
    model = Supplier
    context_object_name = 'suppliers'


class SupplierDetailView(DetailView):
    '''
    Detail view for the Supplier model
    '''
    model = Supplier
    context_object_name = 'supplier'


class SupplierCreateView(CreateView):
    '''
    Create view for the Supplier model
    '''
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:list')


class SupplierUpdateView(UpdateView):
    '''
    Update view for the Supplier model
    '''
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:list')


class SupplierDeleteView(DeleteView):
    '''
    Delete view for the Supplier model
    '''
    model = Supplier
    success_url = reverse_lazy('suppliers:list')
