'''
Forms for the customers app
'''
from django import forms
from localflavor.br.forms import BRCPFField, BRCNPJField  # Import BRCPFField and BRCNPJField
from .models import Customer


class CustomerForm(forms.ModelForm):
    '''
    Form for the Customer model
    '''
    cpf = BRCPFField(required=False)
    cnpj = BRCNPJField(required=False)

    class Meta:
        model = Customer
        fields = '__all__'
