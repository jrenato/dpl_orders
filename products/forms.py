'''
Forms for the products app
'''
from django import forms

from django_select2 import forms as s2forms

from .models import Product


class ProductCategoryWidget(s2forms.ModelSelect2Widget):
    '''
    Widget for the Category model
    '''
    search_fields = [
        'name__icontains',
    ]


class ProductForm(forms.ModelForm):
    '''
    Form for the Product model
    '''
    release_date = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'type': 'date'
            }
        ),
        required=False
    )

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': ProductCategoryWidget,
        }
