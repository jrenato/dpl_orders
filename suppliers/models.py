from django.db import models


class Supplier(models.Model):
    vl_id = models.IntegerField(blank=True, null=True)

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, blank=True, null=True)

    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class SupplierAddress(models.Model):
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE)

    street = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.state} {self.postal_code}'
