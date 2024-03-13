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
    class Meta:
        model = ProductGroup
        fields = '__all__'
