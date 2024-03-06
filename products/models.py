'''
Models for the Products app
'''
from django.conf import settings

from django.db import models
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
    internal_id = models.CharField(_('Internal id'), max_length=20, blank=True, null=True)
    supplier_internal_id = models.CharField(
        _('Supplier Internal id'), max_length=40, blank=True, null=True
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
    release_date = models.DateField(_('Release Date'), blank=True, null=True)
    stock = models.IntegerField(_('Stock'), default=0)
    description = models.TextField(_('Description'), blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified at'), auto_now=True)

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
        if settings.VL_INTEGRATION and not self.internal_id and valid_isbn:
            livro = None
            try:
                livro = Livros.objects.get(isbn1=isbn)
            except Livros.DoesNotExist:
                pass

            if livro:
                self.internal_id = livro.nbook

        # Try to get the product data from the internal id
        if self.internal_id and settings.VL_INTEGRATION:
            livro = Livros.objects.get(nbook=self.internal_id)
            self.name = livro.title
            self.price = livro.sellpr

            if not self.category:
                espec = Espec.objects.get(codigo=livro.subj1)
                if espec.nome in ['HQ', 'MANGÁ', 'LIVRO', 'ALBUM']:
                    self.category, _ = ProductCategory.objects.get_or_create(name=espec.nome)

            estoque = Estoque.objects.get(nbook=self.internal_id)
            self.stock = estoque.disp

        super().save(*args, **kwargs)


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    '''
    Post save signal for the product
    '''
    if created:
        ProductReleaseDateHistory.objects.create(
            product=instance, release_date=instance.release_date
        )


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
        Product, on_delete=models.CASCADE, verbose_name=_('Product'),
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
