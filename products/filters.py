import datetime

import django_filters

# import translation
from django.utils.translation import gettext as _

from .models import Product
from .forms import ProductFilterForm


MONTH_CHOICES = (
    (1, _('January')),
    (2, _('February')),
    (3, _('March')),
    (4, _('April')),
    (5, _('May')),
    (6, _('June')),
    (7, _('July')),
    (8, _('August')),
    (9, _('September')),
    (10, _('October')),
    (11, _('November')),
    (12, _('December')),
)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label=_('Name'),
    )
    release_year = django_filters.ChoiceFilter(
        field_name='release_date', lookup_expr='year',
        # Set the choices for the last five years
        choices=[(x, str(x)) for x in range(datetime.date.today().year - 5, datetime.date.today().year + 1)],
        label=_('Release Year'),
    )
    release_month = django_filters.ChoiceFilter(
        field_name='release_date', lookup_expr='month',
        choices=MONTH_CHOICES,
        label=_('Release Month'),
    )

    class Meta:
        model = Product
        form = ProductFilterForm
        fields = ['name', 'supplier', 'release_date']
