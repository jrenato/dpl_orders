'''
Models for Customers app
'''
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from dpl_orders.helpers import slugify_uniquely
from vldados.models import Cliforn


CUSTOMER_TYPES = (
    ('F', _('Person')),
    ('J', _('Company')),
)

class Customer(models.Model):
    '''
    Customer model
    '''
    vl_id = models.CharField(_('Internal id'), max_length=20, blank=True, null=True)

    name = models.CharField(_('Name'), max_length=120)
    company_name = models.CharField(_('Company Name'), max_length=120, blank=True, null=True)
    short_name = models.CharField(_('Short Name'), max_length=60, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, blank=True, null=True)
    sheet_label = models.CharField(_('Sheet Label'), max_length=60, blank=True, null=True)

    person_or_company = models.CharField(
        _('Person or Company'), max_length=1, choices=CUSTOMER_TYPES, default='J'
    )
    cnpj = models.CharField(_('CNPJ'), max_length=18, blank=True, null=True)
    cpf = models.CharField(_('CPF'), max_length=14, blank=True, null=True)

    state_registration = models.CharField(
        _('State Registration'), max_length=20, blank=True, null=True
    )
    municipal_registration = models.CharField(
        _('Municipal Registration'), max_length=20, blank=True, null=True
    )

    contact_person = models.CharField(_('Contact Person'), max_length=120, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    emailnfe = models.EmailField(_('Email NFe'), blank=True, null=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    vl_created = models.DateTimeField(_('Vialogos Created at'), blank=True, null=True)
    vl_updated = models.DateTimeField(_('Vialogos Updated at'), blank=True, null=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        ordering = ['short_name']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        return reverse('customers:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        '''
        Save the model
        '''
        if not self.id:
            self.slug = slugify_uniquely(self.name, self.__class__)

        cliforn = None
        vl_updated_at = None

        if self.vl_id:
            cliforn = Cliforn.objects.get(codigo=self.vl_id)
            vl_updated_at = cliforn.dtatual

        if not self.vl_updated or (self.vl_updated <= vl_updated_at):
            # Basic data update
            self.name = cliforn.nome
            # Customers don't have short name in vldados
            # self.short_name = cliforn.shortn
            self.company_name = cliforn.razsocial

            self.person_or_company = cliforn.fj
            if self.person_or_company == 'J':
                self.cnpj = cliforn.cgc
                self.cpf = None
            else:
                self.cnpj = None
                self.cpf = cliforn.cgc

            self.state_registration = cliforn.inscr
            self.municipal_registration = cliforn.codmun
            self.contact_person = cliforn.contato
            self.email = cliforn.email
            self.emailnfe = cliforn.emailnfe

            # Address update
            address, _ = CustomerAddress.objects.get_or_create(customer=self)
            address.street = cliforn.endereco
            address.number = cliforn.num
            address.district = cliforn.bairro
            address.city = cliforn.cidade
            address.state = cliforn.estado
            address.zip_code = cliforn.cep
            address.complement = cliforn.complemento
            address.save()

            # Phone numbers update
            for phone_number in [cliforn.telres, cliforn.telcom, cliforn.tel2, cliforn.fax]:
                if not self.phone_number:
                    self.phone_number = phone_number
                else:
                    _, __ = CustomerPhone.objects.get_or_create(
                        customer=self,
                        phone_number=phone_number
                    )

            self.vl_created = cliforn.dtcad
            self.vl_updated = vl_updated_at

        super().save(*args, **kwargs)


class CustomerAddress(models.Model):
    '''
    CustomerAddress model
    '''
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    street = models.CharField(_('Street'), max_length=120)
    number = models.CharField(_('Number'), max_length=10, blank=True, null=True)
    complement = models.CharField(_('Complement'), max_length=120, blank=True, null=True)
    city = models.CharField(_('City'), max_length=120, blank=True, null=True)
    state = models.CharField(_('State'), max_length=2, blank=True, null=True)
    district = models.CharField(_('District'), max_length=120, blank=True, null=True)
    zip_code = models.CharField(_('Zip Code'), max_length=8, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Customer Address')
        verbose_name_plural = _('Customer Addresses')
        ordering = ['customer', 'street']

    def __str__(self):
        return f'{self.street}, {self.number}, {self.city} - {self.state}'

    def get_full_address(self):
        '''
        Return the full address
        '''
        return f'{self.street}, {self.number}, {self.city} - {self.state}'

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        return reverse('customers:detail', args=[self.customer.slug])


class CustomerPhone(models.Model):
    '''
    CustomerPhone model
    '''
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    phone_number = models.CharField(_('Phone'), max_length=15, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Customer Phone')
        verbose_name_plural = _('Customer Phones')
        ordering = ['customer', 'phone_number']

    def __str__(self):
        return f'{self.phone_number}'

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        return reverse('customers:detail', args=[self.customer.slug])
