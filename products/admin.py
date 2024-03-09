'''
Admin for Products
'''
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, ProductGroup,\
    ProductGroupItem, ProductReleaseDateHistory


class ProductGroupItemInline(admin.TabularInline):
    '''
    Inline for the ProductGroupItem model
    '''
    model = ProductGroupItem
    extra = 1
    autocomplete_fields = ['product',]


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


class ProductReleaseDateHistoryInline(admin.TabularInline):
    '''
    Inline for the ProductReleaseDateHistory model
    '''
    model = ProductReleaseDateHistory
    extra = 1
    readonly_fields = ['created',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Admin for the Product model
    '''
    list_display = ('name', 'sku', 'category', 'price', 'stock')
    search_fields = ('name', 'sku', 'supplier_internal_id', 'mb_id', 'vl_id')
    list_filter = ('category', 'supplier',)
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
    inlines = [ProductReleaseDateHistoryInline]

    readonly_fields = ('cover_preview', 'created', 'modified')

    def cover_preview(self, obj):
        cover_imagem = obj.images.filter(is_cover=True).first()
        if cover_imagem:
            return mark_safe(f'<img src="{cover_imagem.image.url}" width="100">')

    # actions = ['make_available', 'make_unavailable']

    # def make_available(self, request, queryset):
    #     queryset.update(available=True)

    # make_available.short_description = 'Marcar como disponível'

    # def make_unavailable(self, request, queryset):
    #     queryset.update(available=False)

    # make_unavailable.short_description = 'Marcar como indisponível'
