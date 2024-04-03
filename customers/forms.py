'''
Forms for the customers app
'''
from django import forms
from django.utils.translation import gettext as _
from django.forms.models import inlineformset_factory

from localflavor.br.forms import BRCPFField, BRCNPJField  # Import BRCPFField and BRCNPJField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Button
from crispy_forms.bootstrap import FormActions, InlineRadios

from .models import Customer, CUSTOMER_TYPES, CustomerAddress, CustomerPhone


class CustomerForm(forms.ModelForm):
    '''
    Form for the Customer model
    '''
    cpf = BRCPFField(required=False)
    cnpj = BRCNPJField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('vl_id', css_class='col-md-4'),
                    Div('short_name', css_class='col-md-4'),
                    Div('slug', css_class='col-md-4'),
                    css_class='row'
                ),
                Div(
                    Div('name', css_class='col-md-6'),
                    Div('company_name', css_class='col-md-6'),
                    css_class='row'
                ),
                Div(
                    Div(InlineRadios('person_or_company'), css_class='col-md-4'),
                    Div('cnpj', css_class='col-md-4'),
                    Div('cpf', css_class='col-md-4'),
                    css_class='row'
                ),
                Div(
                    Div('state_registration', css_class='col-md-6'),
                    Div('municipal_registration', css_class='col-md-6'),
                    css_class='row'
                ),
                Fieldset(
                    _('Contact Details'),
                    Div(
                        Div('contact_person', css_class='col-md-4'),
                        Div('email', css_class='col-md-4'),
                        Div('emailnfe', css_class='col-md-4'),
                        css_class='row'
                    ),
                ),
            ),
            # The form button will be set on the template
            # due to the use of formsets to add address
            # FormActions(
            #     Submit('submit', _('Save'), css_class="btn-success"),
            #     Button('cancel', _('Cancel'), css_class="btn-danger"),
            # ),
        )

        self.fields['cpf'] = BRCPFField(required=False)
        self.fields['cnpj'] = BRCNPJField(required=False)

        self.fields['person_or_company'].widget = forms.RadioSelect()
        self.fields['person_or_company'].choices = CUSTOMER_TYPES

        self.fields['slug'].disabled = True


class CustomerAddressForm(forms.ModelForm):
    '''
    Form for the CustomerAddress model
    '''
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class CustomerPhoneForm(forms.ModelForm):
    '''
    Form for the CustomerPhone model
    '''
    class Meta:
        model = CustomerPhone
        fields = '__all__'


class CustomerAddressFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_tag = False
        self.layout = Layout(
            Div(
                Div('street', css_class='col-md-6'),
                Div('number', css_class='col-md-1'),
                Div('complement', css_class='col-md-5'),
                css_class='row'
            ),
            Div(
                Div('district', css_class='col-md-4'),
                Div('city', css_class='col-md-4'),
                Div('state', css_class='col-md-1'),
                Div('zip_code', css_class='col-md-3'),
                css_class='row'
            ),
        )


class CustomerPhoneFormSetHelper(FormHelper):
    form_tag = False


CustomerAddressFormSet = inlineformset_factory(
    Customer, CustomerAddress, form=CustomerAddressForm, extra=1, can_delete=False
)

CustomerPhoneFormSet = inlineformset_factory(
    Customer, CustomerPhone, form=CustomerPhoneForm, extra=1, can_delete=True
)
