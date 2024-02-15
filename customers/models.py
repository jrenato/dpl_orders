'''
Models for Customers app
'''
from django.db import models


class Customer(models.Model):
    '''
    Customer model
    '''
    name = models.CharField('Nome', max_length=120)
    slug = models.SlugField('Identificador', max_length=120, unique=True)
    short_name = models.CharField('Nome reduzido', max_length=50, unique=True)
    email = models.EmailField('E-mail', blank=True, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, blank=True, unique=True)
    cpf = models.CharField('CPF', max_length=11, blank=True, unique=True)
    phone = models.CharField('Telefone', max_length=20)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class CustomerAddress(models.Model):
    '''
    CustomerAddress model
    '''
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    street = models.CharField('Logradouro', max_length=100)
    number = models.CharField('Número', max_length=15)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)
    state = models.CharField('Estado', max_length=50, blank=True, null=True)
    zip_code = models.CharField('CEP', max_length=10, blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = 'Endereço de Cliente'
        verbose_name_plural = 'Endereços de Clientes'
        ordering = ['customer', 'street']

    def __str__(self):
        return f'{self.street}, {self.number}, {self.city} - {self.state}'
