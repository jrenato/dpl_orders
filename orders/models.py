'''
Models for Orders app
'''
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.utils import formats
from django.dispatch import receiver


ORDER_STATUS_CHOICES = (
    ('PE', _('Pending')),
    ('IS', _('In Separation')),
    ('WC', _('Waiting for Confirmation')),
    ('IN', _('Invoiced')),
    ('WT', _('Waiting Transport')),
    ('FI', _('Finished')),
    ('CA', _('Canceled')),
)


class Order(models.Model):
    '''
    Model for Order
    '''
    vl_id = models.CharField(_('Internal ID'), max_length=100, blank=True, null=True)

    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
        default='PE',
    )

    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE,
        verbose_name=_('Customer'), related_name='orders',
    )

    product_group = models.ForeignKey(
        'product_groups.ProductGroup', on_delete=models.CASCADE,
        verbose_name=_('Product Group'), related_name='orders',
        blank=True, null=True
    )

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)
    canceled = models.DateTimeField(_('Canceled at'), blank=True, null=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ('-created',)

    def __str__(self):
        formatted_created = formats.date_format(self.created, 'SHORT_DATETIME_FORMAT')
        return f'{self.pk} - {self.customer} - {formatted_created}'


class OrderStatusHistory(models.Model):
    '''
    Model for Order Status History
    '''
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        verbose_name=_('Order'),
    )

    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
        default='PE',
    )

    created = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Order Status History')
        verbose_name_plural = _('Order Status Histories')
        ordering = ('-created',)

    def __str__(self):
        return f'{self.created} - {self.status}'

ORDER_ITEM_STATUS_CHOICES = (
    ('PE', _('Pending')),
    ('FI', _('Finished')),
    ('CA', _('Canceled')),
)

class OrderItem(models.Model):
    '''
    Model for Order Item
    '''
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        verbose_name=_('Order'),
        related_name='order_items',
    )

    product = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE,
        verbose_name=_('Product'),
        related_name='order_items',
    )

    status = models.CharField(
        max_length=2,
        choices=ORDER_ITEM_STATUS_CHOICES,
        default='PE',
    )

    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    delivered_quantity = models.PositiveIntegerField(_('Delivered Quantity'), default=0)

    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    discount = models.DecimalField(
        _('Discount'), decimal_places=2, max_digits=10000, blank=True, null=True
    )

    subtotal = models.GeneratedField(
        expression=F('price') * F('quantity'),
        output_field=models.DecimalField(decimal_places=2, max_digits=10000),
        verbose_name=_('Subtotal'),
        db_persist=True,
    )

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)
    canceled = models.DateTimeField(_('Canceled at'), blank=True, null=True)

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_quantity = self.quantity

    def __str__(self):
        return f'"{self.product}" x {self.quantity}'

    def save(self, *args, **kwargs):
        self.price = self.product.price

        if self.id and self.quantity != self.__original_quantity:
            OrderItemHistory.objects.create(
                order_item=self,
                quantity=self.quantity,
                price=self.price
            )
        super().save(*args, **kwargs)

@receiver(post_save, sender=OrderItem)
def order_item_post_save(sender, instance, created, **kwargs):
    '''
    Post save signal for the order item
    '''
    if created:
        OrderItemHistory.objects.create(
            order_item=instance,
            quantity=instance.quantity,
        )


class OrderItemHistory(models.Model):
    '''
    Model for Order Item History
    '''
    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE,
        verbose_name=_('Order Item'),
    )

    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10000, blank=True, null=True
    )
    subtotal = models.GeneratedField(
        expression=F('price') * F('quantity'),
        output_field=models.DecimalField(decimal_places=2, max_digits=10000),
        verbose_name=_('Subtotal'),
        db_persist=True,
    )

    comment = models.TextField(_('Comment'), blank=True, null=True)

    created = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Order Item History')
        verbose_name_plural = _('Order Item Histories')
        ordering = ('-created',)

    def __str__(self):
        return f'{self.created} - {self.quantity}'
