'''
Views for the Product Groups app
'''
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import ProductGroup, ProductGroupItem
from .forms import ProductGroupForm, ProductGroupItemForm


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
    success_url = reverse_lazy('product_groups:list')
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
            .annotate(
                order_items_sum=Sum('product__order_items__quantity', default=0),
            )\
            .order_by('product__name')
        context = super(ProductGroupDetailView, self)\
            .get_context_data(object_list=object_list, **kwargs)
        return context


class ProductGroupUpdateView(PermissionRequiredMixin, UpdateView):
    '''
    Update view for the Product Group model
    '''
    model = ProductGroup
    form_class = ProductGroupForm
    success_url = reverse_lazy('product_groups:list')
    permission_required = 'products.change_productgroup'


class ProductGroupDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Product Group model
    '''
    model = ProductGroup
    success_url = reverse_lazy('product_groups:list')
    permission_required = 'products.delete_productgroup'


### Product Group Item views


class ProductGroupItemCreateView(PermissionRequiredMixin, CreateView):
    '''
    Create view for the Product Group Item model
    '''
    model = ProductGroupItem
    form_class = ProductGroupItemForm
    permission_required = 'products.add_productgroupitem'

    def get_form_kwargs(self):
        if 'slug' not in self.kwargs:
            raise ValueError('Missing pk in kwargs')

        product_group = ProductGroup.objects.get(slug=self.kwargs.get('slug'))
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'group': product_group}

        return kwargs

    def get_success_url(self):
        return reverse_lazy('product_groups:detail', kwargs={'slug': self.object.group.slug})


class ProductGroupItemDeleteView(PermissionRequiredMixin, DeleteView):
    '''
    Delete view for the Product Group Item model
    '''
    model = ProductGroupItem
    permission_required = 'products.delete_productgroupitem'

    def get_success_url(self):
        return reverse_lazy('product_groups:detail', kwargs={'slug': self.object.group.slug})
