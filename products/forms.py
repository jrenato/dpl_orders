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
        fields = ['supplier', 'release_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('supplier', css_class='form-group col-md-4'),
                Div('release_month', css_class='form-group col-md-4'),
                Div('release_year', css_class='form-group col-md-4'),
                css_class='row'
            ),
            FormActions(
                Submit('submit', 'Filter'),
                Button('clear', 'Clear')
            )
        )
