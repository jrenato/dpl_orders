'''
Models for the Products app
'''
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    '''
    Model for the Product Category
    '''
    name = models.CharField(_('Name'), max_length=60)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    '''
    Model for the Product
    '''
    internal_id = models.CharField(_('Internal id'), max_length=20, blank=True, null=True)
    supplier_internal_id = models.CharField(_('Supplier id'), max_length=40, blank=True, null=True)

    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE, verbose_name=_('Supplier'),
    )
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE,
        verbose_name=_('Category'), blank=True, null=True,
    )

    name = models.CharField(_('Name'), max_length=120)
    slug = models.SlugField(_('Slug'), max_length=120, unique=True, blank=True, null=True)
    isbn = models.CharField(_('ISBN'), max_length=13, blank=True, null=True)
    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    stock = models.IntegerField(_('Stock'), blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
