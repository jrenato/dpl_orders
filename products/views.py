'''
Views for the products app
'''
import datetime

from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,\
    TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from django_filters.views import FilterView

from .models import Product
from .forms import ProductForm
from .filters import ProductFilter


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


class ProductFilterView(PermissionRequiredMixin, FilterView):
    '''
    Filter view for the Product model
    '''
    model = Product
    filterset_class = ProductFilter
    paginate_by = 20
    context_object_name = 'products'
    permission_required = 'products.view_product'

    def get_context_data(self, *args, **kwargs):
        _request_copy = self.request.GET.copy()
        parameters = _request_copy.pop('page', True) and _request_copy.urlencode()
        context = super().get_context_data(*args, **kwargs)
        context['parameters'] = parameters
        return context


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


class ProductReleasesListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Product Releases
    '''
    model = Product
    context_object_name = 'products'
    #paginate_by = 20
    template_name = 'products/product_releases_list.html'
    permission_required = 'products.view_product'

    def get_queryset(self):
        # Release date should be equal or greater than last 12 months
        queryset = self.model.objects.filter(
            release_date__gte=datetime.date.today()
        )\
        .select_related('category', 'supplier')\
        .annotate(
            order_items_sum=Sum('order_items__quantity', default=0),
            groups_count=Count('group_items', distinct=True),
        )\
        .order_by('-release_date__year', 'release_date__month', 'supplier__name', 'name')
        return queryset


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


class PostponedReleasesListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Postponed Releases
    '''
    model = Product
    context_object_name = 'products'
    template_name = 'products/postponed_releases_list.html'
    paginate_by = 20
    permission_required = 'products.view_product'

    def get_queryset(self):
        # Filter products with release_dates count greater than 1
        queryset = super().get_queryset()
        queryset = queryset\
            .annotate(release_dates_count=Count('release_dates'))\
            .filter(release_dates_count__gt=1, release_date__gte=datetime.date.today())\
            .select_related('supplier')\
            .prefetch_related('release_dates')\
            .order_by('supplier__name', 'name',)

        return queryset
