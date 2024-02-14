from django.contrib import admin

from .models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created', 'modified', 'available')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'stock', 'available')
    list_per_page = 20
    # actions = ['make_available', 'make_unavailable']

    # def make_available(self, request, queryset):
    #     queryset.update(available=True)

    # make_available.short_description = 'Marcar como disponível'

    # def make_unavailable(self, request, queryset):
    #     queryset.update(available=False)

    # make_unavailable.short_description = 'Marcar como indisponível'
