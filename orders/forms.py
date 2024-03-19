'''
Forms for the orders app
'''
from django import forms
from django_select2 import forms as s2forms
#from django.utils.translation import gettext_lazy as _

from .models import Order
# from products.models import Product, ProductGroup
# from customers.models import Customer


class CustomerWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
        "cnpj__icontains",
    ]


class ProductGroupWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
    ]


class OrderForm(forms.ModelForm):
    # products = forms.ModelMultipleChoiceField(
    #     queryset=Product.objects.all(),
    #     widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    #     required=True
    # )

    # created = forms.DateTimeField(
    #     required=False, label=_('Created at'),
    #     widget=forms.TextInput(attrs={'disabled': 'disabled'})
    # )

    # canceled = forms.DateTimeField(
    #     required=False, label=_('Canceled at'),
    #     widget=forms.TextInput(attrs={'disabled': 'disabled'})
    # )

    class Meta:
        model = Order
        exclude = ('canceled',)
        widgets = {
            "customer": CustomerWidget,
            "product_group": ProductGroupWidget
        }
