'''
Admin for Products
'''
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, ProductReleaseDateHistory, ProductImage


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


class ProductImageInline(admin.TabularInline):
    '''
    Inline for the ProductImage model
    '''
    model = ProductImage
    extra = 1


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

    readonly_fields = ('cover_preview', 'created', 'updated')

    inlines = [ProductImageInline]

    def cover_preview(self, obj):
        cover_image = obj.images.filter(is_main=True).first()
        if cover_image:
            return mark_safe(f'<img src="{cover_image.image.url}" width="100">')

    # actions = ['make_available', 'make_unavailable']

    # def make_available(self, request, queryset):
    #     queryset.update(available=True)

    # make_available.short_description = 'Marcar como disponível'

    # def make_unavailable(self, request, queryset):
    #     queryset.update(available=False)

    # make_unavailable.short_description = 'Marcar como indisponível'
