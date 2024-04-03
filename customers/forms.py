'''
Forms for the customers app
'''
from django import forms
from django.forms.models import inlineformset_factory

from localflavor.br.forms import BRCPFField, BRCNPJField  # Import BRCPFField and BRCNPJField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .models import Customer, CustomerAddress, CustomerPhone


class CustomerForm(forms.ModelForm):
    '''
    Form for the Customer model
    '''
    cpf = BRCPFField(required=False)
    cnpj = BRCNPJField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'


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


CustomerAddressFormSet = inlineformset_factory(
    Customer, CustomerAddress, form=CustomerAddressForm, extra=1, can_delete=False
)

CustomerPhoneFormSet = inlineformset_factory(
    Customer, CustomerPhone, form=CustomerPhoneForm, extra=1, can_delete=True
)


class CustomerFormHelper(FormHelper):
    form_tag = False


class CustomerAddressFormSetHelper(FormHelper):
    form_tag = False


class CustomerPhoneFormSetHelper(FormHelper):
    form_tag = False
