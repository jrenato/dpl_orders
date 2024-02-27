'''
Models for the Suppliers app
'''
from django.db import models
from django.utils.translation import gettext_lazy as _

from dpl_orders.helpers import slugify_uniquely

from vldados.models import Cliforn


class Supplier(models.Model):
    '''
    Model for the Supplier
    '''
    internal_id = models.CharField(_('Internal id'), max_length=20, blank=True, null=True)

    name = models.CharField(_('Name'), max_length=120)
    company_name = models.CharField(_('Company Name'), max_length=120, blank=True, null=True)
    short_name = models.CharField(_('Short Name'), max_length=60, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, blank=True, null=True)

    cnpj = models.CharField(_('CNPJ'), max_length=18, blank=True, null=True)
    contact_person = models.CharField(_('Contact Person'), max_length=120, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        # TODO: Change the url to the correct one
        return f'/suppliers/{self.slug}'

    def save(self, *args, **kwargs):
        '''
        Save the model
        '''
        if not self.id:
            self.slug = slugify_uniquely(self.name, self.__class__)

        # TODO: Retrieve all the data from the Cliforn model
        if self.internal_id:
            cliforn, _ = Cliforn.objects.get(codigo=self.internal_id)
            self.name = cliforn.nome
            self.cnpj = cliforn.cgc
        super().save(*args, **kwargs)


class SupplierCNPJ(models.Model):
    '''
    Model for the Supplier CNPJ
    '''
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

    cnpj = models.CharField(_('CNPJ'), max_length=18, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Supplier CNPJ')
        verbose_name_plural = _('Supplier CNPJs')
        ordering = ['supplier', 'cnpj']

    def __str__(self):
        return f'{self.cnpj}'


class SupplierAddress(models.Model):
    '''
    Model for the Supplier Address
    '''
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

    street = models.CharField(_('Street'), max_length=120)
    number = models.CharField(_('Number'), max_length=10)
    complement = models.CharField(_('Complement'), max_length=120, blank=True, null=True)
    city = models.CharField(_('City'), max_length=120, blank=True, null=True)
    state = models.CharField(_('State'), max_length=2, blank=True, null=True)
    zip_code = models.CharField(_('Zip Code'), max_length=8, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Supplier Address')
        verbose_name_plural = _('Supplier Addresses')
        ordering = ['supplier', 'street']

    def __str__(self):
        return f'{self.street}, {self.number} - {self.city} - {self.state} - CEP {self.zip_code}'
