from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    vl_id = models.IntegerField('ID do Vialogos', blank=True, null=True)
    supplier_id = models.IntegerField('ID do Fornecedores', blank=True, null=True)

    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=120)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
