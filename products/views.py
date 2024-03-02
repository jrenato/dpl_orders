'''
Views for the products app
'''

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Product
from .forms import ProductForm


class ProductListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Product model
    '''
    model = Product
    context_object_name = 'products'
    permission_required = 'products.view_product'


class ProductDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Product model
    '''
    model = Product
    context_object_name = 'product'
    permission_required = 'products.view_product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Product model
    '''
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')
    permission_required = 'products.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Product model
    '''
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')
    permission_required = 'products.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Product model
    '''
    model = Product
    success_url = reverse_lazy('products:list')
    permission_required = 'products.delete_product'
