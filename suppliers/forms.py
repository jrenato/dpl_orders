'''
Forms for the suppliers app
'''
from django import forms
from django.utils.translation import gettext as _

from localflavor.br.forms import BRCPFField, BRCNPJField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, HTML, Div

from .models import Supplier


class SupplierForm(forms.ModelForm):
    '''
    Form for the Supplier model
    '''
    # cpf = BRCPFField(required=False)
    # cnpj = BRCNPJField(required=False)

    class Meta:
        model = Supplier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('vl_id', css_class='col-md-3'),
                    Div('mb_id', css_class='col-md-3'),
                    Div('short_name', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('name', css_class='col-md-6'),
                    Div('company_name', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div('person_or_company', css_class='col-md-2'),
                    Div('cnpj', css_class='col-md-5'),
                    Div('cpf', css_class='col-md-5'),
                    css_class='row'
                ),
                Div(
                    Div('state_registration', css_class='col-md-4'),
                    Div('municipal_registration', css_class='col-md-8'),
                    css_class='row'
                ),
                Fieldset(
                    _('Contact Details'),
                    Div(
                        Div('contact_person', css_class='col-md-6'),
                        Div('phone_number', css_class='col-md-6'),
                        css_class='row'
                    ),
                    Div(
                        Div('email', css_class='col-md-6'),
                        Div('emailnfe', css_class='col-md-6'),
                        css_class='row'
                    ),
                ),
            ),
            Submit('submit', _('Save'), css_class="btn-success"),
        )

        self.fields['cpf'] = BRCPFField(required=False)
        self.fields['cnpj'] = BRCNPJField(required=False)
