'''
Models for the Product Groups app
'''
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from dpl_orders.helpers import slugify_uniquely


PRODUCT_GROUP_STATUS = [
    ('PE', _('Pending')),
    ('OR', _('Ordered')),
    ('SE', _('In Separation')),
    ('FI', _('Finished')),
    ('CA', _('Canceled')),
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
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

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
        return reverse('products:group_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify_uniquely(self.name, self.__class__)
        super().save(*args, **kwargs)


class ProductGroupItem(models.Model):
    '''
    Model for the Product Group Item
    '''
    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE, verbose_name=_('Product'),
        related_name='group_items'
    )
    group = models.ForeignKey(
        ProductGroup, on_delete=models.CASCADE, verbose_name=_('Group'),
        related_name='group_items'
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

