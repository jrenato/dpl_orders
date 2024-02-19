'''
Models for the Product Group
'''
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    products = models.ManyToManyField(
        'products.Product', verbose_name=_('Products'), related_name='product_groups', blank=True
    )

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
