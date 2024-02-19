from django.db import models
from django.utils.translation import gettext_lazy as _


ORDER_STATUS_CHOICES = (
    ('PE', _('Pending')),
    ('IS', _('In Separation')),
    ('WC', _('Waiting for Confirmation')),
    ('IN', _('Invoiced')),
    ('WT', _('Waiting Transport')),
    ('FI', _('Finished')),
    ('CA', _('Cancelled')),
)