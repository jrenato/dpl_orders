'''
Models for the Products app
'''
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

from dpl_orders.helpers import slugify_uniquely
from vldados.models import Livros, Espec, Estoque


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
    vl_id = models.CharField(_('Vialogos id'), max_length=20, blank=True, null=True)
    mb_id = models.CharField(_('Metabooks id'), max_length=64, blank=True, null=True)
    supplier_internal_id = models.CharField(
        _('Supplier Internal id'), max_length=64, blank=True, null=True
    )

    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE,
        related_name='products', verbose_name=_('Supplier'),
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
    mb_price = models.DecimalField(
        _('Metabooks Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    vl_price = models.DecimalField(
        _('Vialogos Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )

    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    stock = models.IntegerField(_('Stock'), default=0)
    description = models.TextField(_('Description'), blank=True, null=True)

    mb_created = models.DateField(_('Metabooks created at'), blank=True, null=True)
    mb_updated = models.DateField(_('Metabooks updated at'), blank=True, null=True)

    vl_created = models.DateField(_('Vialogos created at'), blank=True, null=True)
    vl_updated = models.DateField(_('Vialogos updated at'), blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

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
        return reverse('products:detail', args=[self.slug])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._release_date = self.release_date

    def save(self, *args, **kwargs):
        # If the product is being created, generate the slug
        if not self.id:
            self.slug = slugify_uniquely(self.name, self.__class__)
        elif self.release_date and self._release_date != self.release_date:
            ProductReleaseDateHistory.objects.create(
                product=self, release_date=self.release_date
            )

        # Try to get the internal id from the isbn
        isbn = f'{self.sku}'
        valid_isbn = isbn and isbn.startswith('978') and len(isbn) == 13
        if settings.VL_INTEGRATION and not self.vl_id and valid_isbn:
            livro = None
            try:
                livro = Livros.objects.get(isbn1=isbn)
            except Livros.DoesNotExist:
                pass
            except Livros.MultipleObjectsReturned as exc:
                raise Livros.MultipleObjectsReturned(
                    f'Multiple books for {isbn} - {self.name}') from exc

            if livro:
                self.vl_id = livro.nbook

        # Try to get the product data from the internal id
        if self.vl_id and settings.VL_INTEGRATION:
            livro = Livros.objects.get(nbook=self.vl_id)
            #self.name = livro.title
            self.vl_price = livro.sellpr
            if not self.price or self.price < self.vl_price:
                self.price = self.vl_price

            if not self.category:
                espec = Espec.objects.filter(codigo=livro.subj1).first()
                if espec and espec.nome in ['HQ', 'MANGÁ', 'LIVRO', 'ALBUM']:
                    self.category, _ = ProductCategory.objects.get_or_create(name=espec.nome)

            try:
                estoque = Estoque.objects.get(nbook=self.vl_id, filial='01')
            except Estoque.DoesNotExist:
                estoque = None
            except Estoque.MultipleObjectsReturned as exc:
                raise Estoque.MultipleObjectsReturned(
                    f'Multiple stocks for {self.vl_id} - {self.name}') from exc

            if estoque:
                self.stock = estoque.disp

        super().save(*args, **kwargs)


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    '''
    Post save signal for the product
    '''
    if created and instance.release_date:
        ProductReleaseDateHistory.objects.create(
            product=instance, release_date=instance.release_date
        )


class ProductImage(models.Model):
    '''
    Model for the Product Image
    '''
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_('Product'), related_name='images'
    )
    image = models.ImageField(_('Image'), upload_to='products/images')
    is_main = models.BooleanField(_('Is Cover'), default=False)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        '''
        Meta options
        '''
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
        ordering = ['product', '-created']

    def __str__(self):
        return f'{self.product.name} - {self.image}'


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
        ordering = ['product', '-created']

    def __str__(self):
        return f'{self.product.name} - {self.release_date}'
