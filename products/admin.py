'''
Admin for Products
'''
from django.contrib import admin

from .models import ProductCategory, Product, ProductGroup, ProductGroupItem


class ProductGroupItemInline(admin.TabularInline):
    '''
    Inline for the ProductGroupItem model
    '''
    model = ProductGroupItem
    extra = 1


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    '''
    Admin for the Product Group
    '''
    list_display = ['name', 'status', 'customer_limit_date', 'supplier_limit_date',]
    search_fields = ['name', 'status',]
    list_filter = ['status', 'customer_limit_date', 'supplier_limit_date',]
    date_hierarchy = 'supplier_limit_date'
    readonly_fields = ['created', 'modified']
    inlines = [ProductGroupItemInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    '''
    Admin for the ProductCategory model
    '''
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Admin for the Product model
    '''
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock')
    list_per_page = 20
    # actions = ['make_available', 'make_unavailable']

    # def make_available(self, request, queryset):
    #     queryset.update(available=True)

    # make_available.short_description = 'Marcar como disponível'

    # def make_unavailable(self, request, queryset):
    #     queryset.update(available=False)

    # make_unavailable.short_description = 'Marcar como indisponível'
