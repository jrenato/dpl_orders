'''
Views for the products app
'''
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,\
    TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Product, ProductGroup, ProductGroupItem
from .forms import ProductForm, ProductGroupForm


class ProductListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Product model
    '''
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()\
            .select_related('category', 'supplier')\
            .annotate(
                order_items_sum=Sum('order_items__quantity'),
                groups_count=Count('group_items', distinct=True),
            )\
            .order_by('name')

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


### Product Group views


class ProductGroupListView(PermissionRequiredMixin, ListView):
    '''
    List view for the Product Group model
    '''
    model = ProductGroup
    context_object_name = 'product_groups'
    paginate_by = 20
    permission_required = 'products.view_productgroup'

    def get_queryset(self):
        # Annotato group_items count
        queryset = super().get_queryset()\
            .annotate(
                items_count=Count('group_items', distinct=True),
            )
        return queryset


class ProductGroupCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Product Group model
    '''
    model = ProductGroup
    form_class = ProductGroupForm
    success_url = reverse_lazy('products:group-list')
    permission_required = 'products.add_productgroup'


class ProductGroupDetailView(PermissionRequiredMixin, MultipleObjectMixin, DetailView):
    '''
    Detail view for the Product Group model
    '''
    model = ProductGroup
    #context_object_name = 'product_group'
    paginate_by = 20
    permission_required = 'products.view_productgroup'

    def get_queryset(self):
        # Prefetch group_items
        queryset = super().get_queryset()\
            .prefetch_related('group_items', 'group_items__product')
        return queryset

    def get_context_data(self, **kwargs):
        object_list = self.get_object().group_items\
            .select_related('product', 'product__category', 'product__supplier')\
            .order_by('product__name')
        context = super(ProductGroupDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context

    # def get_context_data(self, **kwargs):
    #     # object_list = self.get_object().group_items.annotate(
    #     #     order_items_sum=Sum('order_items__quantity'),
    #     # )
    #     object_list = ProductGroupItem.objects\
    #         .filter(group=self.get_object())\
    #         .select_related('product', 'product__category', 'product__supplier', 'product__order_items')\
    #         .annotate(
    #             order_items_sum=Sum('product__order_items__quantity'),
    #         )\
    #         .order_by('product__name')

    #     context = super(ProductGroupDetailView, self)\
    #         .get_context_data(object_list=object_list, **kwargs)

    #     return context


class ProductGroupUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Product Group model
    '''
    model = ProductGroup
    form_class = ProductGroupForm
    success_url = reverse_lazy('products:group-list')
    permission_required = 'products.change_productgroup'


class ProductGroupDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Product Group model
    '''
    model = ProductGroup
    success_url = reverse_lazy('products:group-list')
    permission_required = 'products.delete_productgroup'


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
