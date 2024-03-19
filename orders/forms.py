'''
Forms for the orders app
'''
from django import forms
from django.utils.translation import gettext_lazy as _

from django_select2 import forms as s2forms

from .models import Order, OrderItem


class CustomerWidget(s2forms.ModelSelect2Widget):
    '''
    Widget for the Customer model
    '''
    search_fields = [
        'name__icontains',
        'cnpj__icontains',
    ]


class ProductGroupWidget(s2forms.ModelSelect2Widget):
    '''
    Widget for the ProductGroup model
    '''
    search_fields = [
        'name__icontains',
    ]


class ProductWidget(s2forms.ModelSelect2Widget):
    '''
    Widget for the Product model
    '''
    search_fields = [
        'name__icontains',
        'sku__icontains',
        'supplier_internal_id__icontains',
    ]


class OrderCreateForm(forms.ModelForm):
    '''
    Form to create an Order
    '''
    class Meta:
        model = Order
        fields = 'vl_id', 'customer', 'product_group'
        widgets = {
            'customer': CustomerWidget,
            'product_group': ProductGroupWidget,
        }


class OrderUpdateForm(forms.ModelForm):
    '''
    Form to update an Order
    '''
    class Meta:
        model = Order
        fields = 'vl_id', 'customer', 'product_group'
        widgets = {
            'customer': CustomerWidget,
            'product_group': ProductGroupWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].disabled = True
        self.fields['product_group'].disabled = True


class OrderItemCreateForm(forms.ModelForm):
    '''
    Form to create an OrderItem
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].disabled = True

    class Meta:
        model = OrderItem
        fields = 'order', 'product', 'quantity', 'discount'
        widgets = {
            'product': ProductWidget,
        }


class OrderItemUpdateForm(forms.ModelForm):
    '''
    Form to update an OrderItem
    '''
    class Meta:
        model = OrderItem
        fields = 'order', 'product', 'quantity', 'discount'
        widgets = {
            'product': ProductWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].disabled = True
        self.fields['product'].disabled = True
