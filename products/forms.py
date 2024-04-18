'''
Forms for the products app
'''
from django import forms

from django_select2 import forms as s2forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Button, Row, Column
from crispy_forms.bootstrap import FormActions, InlineRadios

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


class ProductFilterForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['price', 'release_date', 'supplier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('device_created', css_class='form-group col-12'),
                css_class='form-row'
            ),
            Row(
                Column('device_id', css_class='form-group col-12'),
                css_class='form-row'
            ),
            Row(
                Column('device_type', css_class='form-group col-6 mb-0'),
                Column('device_group', css_class='form-group col-6 mb-0'),
                css_class='form-row'
            ),
        )
