'''
Models for the Products app
'''
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
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
    slug = models.SlugField(_('Slug'), max_length=140, unique=True, blank=True, null=True)
    sku = models.CharField(_('SKU'), max_length=13, blank=True, null=True)
    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    stock = models.IntegerField(_('Stock'), default=0)
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

    def get_absolute_url(self):
        '''
        Return the absolute url for the product
        '''
        # TODO: Change the url to the correct one
        return f'/products/{self.slug}/'

    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        if new_slug != self.slug:
            self.slug = new_slug
            i = 1
            while Product.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-{i}'
                i += 1
        super().save(*args, **kwargs)


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
    slug = models.SlugField(_('Slug'), max_length=110, unique=True, null=False)
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

    def get_absolute_url(self):
        '''
        Return the absolute url for the product group
        '''
        # TODO: Change the url to the correct one
        return f'/products/groups/{self.slug}/'

    # Save a copy of the original name
    def __init__(self, *args, **kwargs):
        super(ProductGroup, self).__init__(*args, **kwargs)
        self._original_name = self.name

    # If the name is changed, update the slug.
    # Make sure the slug is unique
    def save(self, *args, **kwargs):
        if self.name != self._original_name:
            self.slug = slugify(self.name)
            i = 1
            while ProductGroup.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-{i}'
                i += 1
        super(ProductGroup, self).save(*args, **kwargs)


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
