from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier
    #template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    #template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    #template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(DeleteView):
    model = Supplier
    #template_name = 'suppliers/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')
