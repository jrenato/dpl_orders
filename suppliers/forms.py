from django import forms
from localflavor.br.forms import BRCPFField, BRCNPJField  # Import BRCPFField and BRCNPJField
from .models import Supplier


class SupplierForm(forms.ModelForm):
    cpf = BRCPFField(required=False)
    cnpj = BRCNPJField(required=False)

    class Meta:
        model = Supplier
        fields = [
            'name',
            'short_name',
            'cpf',
            'cnpj',
            'contact_person',
            'email',
            'phone_number',
        ]
