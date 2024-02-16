'''
Models for the Products app
'''
from django.db import models


class ProductCategory(models.Model):
    '''
    Model for the Product Category
    '''
    name = models.CharField('Nome', max_length=100)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Categoria de Produto'
        verbose_name_plural = 'Categorias de Produtos'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    '''
    Model for the Product
    '''
    vl_id = models.IntegerField('Código do Vialogos', blank=True, null=True)
    supplier_code = models.IntegerField('Código do Fornecedor', blank=True, null=True)

    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE, verbose_name='Fornecedor'
    )
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Categoria',
    )

    name = models.CharField('Nome', max_length=120)
    slug = models.SlugField('Slug', max_length=120, unique=True, blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=13, blank=True, null=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=10000, blank=True, null=True)
    release_date = models.DateField('Data de lançamento', blank=True, null=True)
    stock = models.IntegerField('Estoque', blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
