'''
Forms for the customers app
'''
from django import forms

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


class CustomerFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'name',
            'short_name',
            'slug',
            'email',
            'cpf',
            'cnpj',
        )
        self.render_required_fields = True


class CustomerAddressForm(forms.ModelForm):
    '''
    Form for the CustomerAddress model
    '''
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class CustomerAddressFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'street',
            'number',
            'complement',
            'city',
            'state',
            'district',
            'zip_code',
        )
        self.render_required_fields = True


class CustomerPhoneForm(forms.ModelForm):
    '''
    Form for the CustomerPhone model
    '''
    class Meta:
        model = CustomerPhone
        fields = '__all__'


class CustomerPhoneFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'phone_number',
        )
        self.render_required_fields = True
