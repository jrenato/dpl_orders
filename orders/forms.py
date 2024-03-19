from django import forms

from django.utils.translation import gettext_lazy as _

from .models import Order
from products.models import Product


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

    canceled = forms.DateTimeField(
        required=False, label=_('Canceled at'),
        widget=forms.TextInput(attrs={'disabled': 'disabled'})
    )

    class Meta:
        model = Order
        fields = '__all__'
