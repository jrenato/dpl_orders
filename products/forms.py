'''
Forms for the products app
'''
from django import forms
from .models import Product, ProductGroup


class ProductForm(forms.ModelForm):
    '''
    Form for the Product model
    '''
    class Meta:
        model = Product
        fields = '__all__'


class ProductGroupForm(forms.ModelForm):
    '''
    Form for the Product Group model
    '''
    slug = forms.SlugField(max_length=110, widget=forms.HiddenInput())
    customer_limit_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    supplier_limit_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = ProductGroup
        fields = '__all__'
