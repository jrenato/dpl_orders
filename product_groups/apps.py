from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductGroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_groups'
    verbose_name = _('Product Groups')
