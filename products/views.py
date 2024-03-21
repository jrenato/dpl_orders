'''
Views for the products app
'''
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,\
    TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Product
from .forms import ProductForm


class ProductListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Product model
    '''
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Check if the query is present
        # (the user is searching for something)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | \
                Q(sku__icontains=query) | \
                Q(vl_id__icontains=query) | \
                Q(supplier_internal_id__icontains=query)
            )

        # Prefetch related fields and annotate relevant data
        queryset = queryset\
            .select_related('category', 'supplier')\
            .annotate(
                order_items_sum=Sum('order_items__quantity', default=0),
                groups_count=Count('group_items', distinct=True),
            )\
            .order_by('name')

        return queryset


class ProductSearchView(ProductListView):
    '''
    Search view for the Product model
    '''
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(\
                Q(name__icontains=query) | \
                Q(sku__icontains=query) | \
                Q(vl_id__icontains=query) | \
                Q(supplier_internal_id__icontains=query)
            )
        return queryset


class ProductDetailView(PermissionRequiredMixin, DetailView):
    '''
    Detail view for the Product model
    '''
    model = Product
    context_object_name = 'product'
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()\
            .select_related('category', 'supplier')\
            .prefetch_related(
                'order_items', 'order_items__order', 'order_items__order__customer',
                'group_items', 'group_items__group',
            )
        return queryset


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


### Debug views


class ProductsDebugTemplateView(TemplateView):
    '''
    Debug view for the Products
    '''
    template_name = 'products/debug.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_without_images'] = Product.objects\
            .annotate(images_count=Count('images')).filter(images_count=0).count()
        return context


class ProductsWithoutImagesListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Products without images
    '''
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset().filter(images__isnull=True)
        return queryset
