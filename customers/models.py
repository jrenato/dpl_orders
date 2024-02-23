'''
Models for Customers app
'''
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    '''
    Customer model
    '''
    internal_id = models.CharField(_('Internal id'), max_length=20, blank=True, null=True)

    name = models.CharField(_('Name'), max_length=120)
    short_name = models.CharField(_('Short Name'), max_length=60, blank=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    cnpj = models.CharField(_('CNPJ'), max_length=14, blank=True, null=True)
    cpf = models.CharField(_('CPF'), max_length=11, blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=15, blank=True, null=True)
    contact_person = models.CharField(_('Contact Person'), max_length=120, blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        # TODO: Change the url to the correct one
        return f'/customers/{self.slug}'

    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        if new_slug != self.slug:
            self.slug = new_slug
            i = 1
            while Customer.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-{i}'
                i += 1
        super().save(*args, **kwargs)


class CustomerAddress(models.Model):
    '''
    CustomerAddress model
    '''
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

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
        verbose_name = _('Customer Address')
        verbose_name_plural = _('Customer Addresses')
        ordering = ['customer', 'street']

    def __str__(self):
        return f'{self.street}, {self.number}, {self.city} - {self.state}'
