'''
Forms for the suppliers app
'''
from django import forms
from django.utils.translation import gettext as _

from localflavor.br.forms import BRCPFField, BRCNPJField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Save')))
        # self.helper.layout = Layout(
        #     Fieldset(
        #         'Supplier',
        #         'name',
        #         'short_name',
        #         'contact_person',
        #         'email',
        #         'phone_number',
        #         'website',
        #         'created',
        #         'updated',
        #     ),
        #     Submit('submit', 'Submit'),
        # )
