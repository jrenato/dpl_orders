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
    supplier_internal_id = models.CharField(
        _('Supplier Internal id'), max_length=40, blank=True, null=True
    )

    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE, verbose_name=_('Supplier'),
        related_name='products', blank=True, null=True
    )

    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, verbose_name=_('Category'),
        related_name='products', blank=True, null=True,
    )

    name = models.CharField(_('Name'), max_length=120)
    slug = models.SlugField(_('Slug'), max_length=120, unique=True, blank=True, null=True)
    sku = models.CharField(_('SKU'), max_length=13, blank=True, null=True)
    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    stock = models.IntegerField(_('Stock'), blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)

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


class ProductReleaseDateHistory(models.Model):
    '''
    Model for the Product Release Date History
    '''
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='release_dates'
    )
    release_date = models.DateField(_('Release Date'))
    created = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Product Release Date History')
        verbose_name_plural = _('Product Release Date Histories')
        ordering = ['product', '-release_date']

    def __str__(self):
        return f'{self.product.name} - {self.release_date}'


PRODUCT_GROUP_STATUS = [
    ('PE', _('Pending')),
    ('OR', _('Ordered')),
    ('SE', _('In Separation')),
    ('FI', _('Finished')),
    ('CA', _('Cancelled')),
    ('AR', _('Archived')),
]


class ProductGroup(models.Model):
    '''
    Model for the Product Group
    '''
    name = models.CharField(_('Name'), max_length=100)
    status = models.CharField(_('Status'), max_length=2, choices=PRODUCT_GROUP_STATUS, default='PE')

    customer_limit_date = models.DateField(_('Limit Date for the Customer'), blank=True, null=True)
    supplier_limit_date = models.DateField(_('Limit Date for the Supplier'), blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Products Group')
        verbose_name_plural = _('Products Groups')
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class ProductGroupItem(models.Model):
    '''
    Model for the Product Group Item
    '''
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'),
        related_name='group_products'
    )
    group = models.ForeignKey(
        ProductGroup, on_delete=models.CASCADE, verbose_name=_('Group'),
        related_name='group_products'
    )

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Product Group Item')
        verbose_name_plural = _('Product Group Items')
        ordering = ['group', 'product']

    def __str__(self):
        return f'{self.group.name} - {self.product.name}'
