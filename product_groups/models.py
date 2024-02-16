'''
Models for the Product Group
'''
from django.db import models


class ProductGroupStatus(models.Model):
    '''
    Model for the Product Group Status
    '''
    name = models.CharField('Nome', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Status do Grupo de Produtos'
        verbose_name_plural = 'Status dos Grupos de Produtos'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class ProductGroup(models.Model):
    '''
    Model for the Product Group
    '''
    name = models.CharField('Nome', max_length=100)
    products = models.ManyToManyField(
        'products.Product', verbose_name='Produtos', blank=True
    )
    status = models.ForeignKey(
        ProductGroupStatus, on_delete=models.CASCADE, verbose_name='Status'
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
