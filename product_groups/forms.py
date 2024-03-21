'''
Forms for the products app
'''
from django import forms

from django_select2 import forms as s2forms

from .models import ProductGroup, ProductGroupItem


class ProductGroupForm(forms.ModelForm):
    '''
    Form for the Product Group model
    '''
    slug = forms.SlugField(
        max_length=110, widget=forms.HiddenInput(),
        required=False
    )
    customer_limit_date = forms.DateField(
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'class': 'form-control', 
                'type': 'date'
            }
        ),
        required=False
    )
    supplier_limit_date = forms.DateField(
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
        model = ProductGroup
        fields = '__all__'


class ProductWidget(s2forms.ModelSelect2Widget):
    '''
    Widget for the Product model
    '''
    search_fields = [
        'name__icontains',
        'sku__icontains',
        'supplier_internal_id__icontains',
    ]


class ProductGroupItemForm(forms.ModelForm):
    '''
    Form for the Product Group Item model
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].disabled = True

    class Meta:
        model = ProductGroupItem
        fields = 'group', 'product'
        widgets = {
            'product': ProductWidget,
        }
