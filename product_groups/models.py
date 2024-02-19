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
    name = models.CharField('Nome', max_length=100)
    status = models.CharField('Status', max_length=2, choices=PRODUCT_GROUP_STATUS, default='PE')
    products = models.ManyToManyField(
        'products.Product', verbose_name='Produtos', blank=True
    )

    customer_limit_date = models.DateField('Data limite para o cliente', blank=True, null=True)
    supplier_limit_date = models.DateField('Data limite para o fornecedor', blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Grupo de Produtos'
        verbose_name_plural = 'Grupos de Produtos'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
