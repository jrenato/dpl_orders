from django.contrib import admin
from .models import Supplier, SupplierAddress


class SupplierAddressInline(admin.StackedInline):  # You can use TabularInline for a more compact view
    model = SupplierAddress
    extra = 1  # Number of inline forms to display


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'contact_person', 'email', 'phone_number')
    search_fields = ('name', 'short_name', 'contact_person', 'email', 'phone_number')
    inlines = [SupplierAddressInline]
