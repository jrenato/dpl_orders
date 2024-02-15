'''
Models for the Suppliers app
'''
from django.db import models


class Supplier(models.Model):
    '''
    Model for the Supplier
    '''
    vl_id = models.IntegerField('Código do Vialogos', blank=True, null=True)

    name = models.CharField('Nome', max_length=100)
    short_name = models.CharField('Nome curto', max_length=50, blank=True, null=True)
    slug = models.SlugField('Slug', max_length=100, unique=True)

    cpf = models.CharField('CPF', max_length=14, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True, null=True)
    contact_person = models.CharField('Contato', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    phone_number = models.CharField('Telefone', max_length=20, blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return f'{self.name}'


class SupplierAddress(models.Model):
    '''
    Model for the Supplier Address
    '''
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

    street = models.CharField('Logradouro', max_length=100)
    number = models.CharField('Número', max_length=15)
    city = models.CharField('Cidade', max_length=50, blank=True, null=True)
    state = models.CharField('Estado', max_length=50, blank=True, null=True)
    zip_code = models.CharField('CEP', max_length=10, blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return f'{self.street}, {self.number} - {self.city} - {self.state} - CEP {self.zip_code}'
