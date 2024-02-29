'''
Forms for the suppliers app
'''
from django import forms
from localflavor.br.forms import BRCPFField, BRCNPJField  # Import BRCPFField and BRCNPJField
from .models import Supplier


class SupplierForm(forms.ModelForm):
    '''
    Form for the Supplier model
    '''
    cpf = BRCPFField(required=False)
    cnpj = BRCNPJField(required=False)

    class Meta:
        model = Supplier
        fields = '__all__'