"""
Models for Customers app handling customer management and related data.
Supports both individual and corporate customers with address and contact information.
"""
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models, transaction
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from dpl_orders.helpers import slugify_uniquely
from vldados.models import Cliforn


class CustomerType(models.TextChoices):
    """Customer type choices"""
    PERSON = 'F', _('Person')
    COMPANY = 'J', _('Company')


class CustomerManager(models.Manager):
    """Customer model manager with common query methods"""
    def get_companies(self):
        """Return only company customers"""
        return self.filter(person_or_company=CustomerType.COMPANY)

    def get_individuals(self):
        """Return only individual customers"""
        return self.filter(person_or_company=CustomerType.PERSON)

    def get_active(self):
        """Return active customers"""
        return self.filter(is_active=True)


class Customer(models.Model):
    """
    Customer model supporting both individual and corporate customers.
    Includes contact information and integration with Vialogos system.
    """
    # Basic information
    name = models.CharField(_('Name'), max_length=120, db_index=True)
    company_name = models.CharField(_('Company Name'), max_length=120, blank=True, null=True)
    short_name = models.CharField(_('Short Name'), max_length=60, blank=True, null=True)
    slug = models.SlugField(
        _('Slug'),
        max_length=140,
        unique=True,
        blank=True,
        db_index=True,
        help_text=_('URL-friendly name (auto-generated)')
    )
    sheet_label = models.CharField(_('Sheet Label'), max_length=60, blank=True, null=True)
    is_active = models.BooleanField(_('Active'), default=True)

    # Customer type and tax information
    person_or_company = models.CharField(
        _('Person or Company'),
        max_length=1,
        choices=CustomerType.choices,
        default=CustomerType.COMPANY
    )
    
    cnpj = models.CharField(
        _('CNPJ'),
        max_length=18,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
                message=_('Enter a valid CNPJ in XX.XXX.XXX/XXXX-XX format')
            )
        ]
    )
    
    cpf = models.CharField(
        _('CPF'),
        max_length=14,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message=_('Enter a valid CPF in XXX.XXX.XXX-XX format')
            )
        ]
    )

    # Registration information
    state_registration = models.CharField(
        _('State Registration'),
        max_length=20,
        blank=True,
        null=True,
        db_index=True
    )
    municipal_registration = models.CharField(
        _('Municipal Registration'),
        max_length=20,
        blank=True,
        null=True
    )

    # Contact information
    contact_person = models.CharField(_('Contact Person'), max_length=120, blank=True, null=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    emailnfe = models.EmailField(_('Email NFe'), blank=True, null=True)
    phone_number = models.CharField(
        _('Primary Phone Number'),
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=_('Enter a valid phone number')
            )
        ]
    )

    # Timestamps
    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    # Vialogos integration fields
    vl_id = models.CharField(
        _('Internal id'),
        max_length=20,
        blank=True,
        null=True,
        db_index=True,
        help_text=_('Vialogos system ID')
    )
    vl_created = models.DateTimeField(_('Vialogos Created at'), blank=True, null=True)
    vl_updated = models.DateTimeField(_('Vialogos Updated at'), blank=True, null=True)

    # Manager
    objects = CustomerManager()

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
        ordering = ['short_name', 'name']
        indexes = [
            models.Index(fields=['name', 'short_name']),
            models.Index(fields=['person_or_company', 'is_active'])
        ]

    def __str__(self):
        return f'{self.short_name or self.name}'

    def get_absolute_url(self):
        """Return the absolute url for the customer"""
        return reverse('customers:detail', args=[self.slug])

    def clean(self):
        """Validate model data"""
        if self.person_or_company == CustomerType.COMPANY and not self.cnpj:
            raise ValidationError(_('CNPJ is required for companies'))
        if self.person_or_company == CustomerType.PERSON and not self.cpf:
            raise ValidationError(_('CPF is required for individuals'))
        if self.cnpj and self.cpf:
            raise ValidationError(_('Customer cannot have both CNPJ and CPF'))

    @transaction.atomic
    def sync_with_vialogos(self):
        """Synchronize customer data with Vialogos system"""
        if not settings.VL_INTEGRATION or not self.vl_id:
            return

        try:
            cliforn = Cliforn.objects.get(codigo=self.vl_id)
            vl_updated_at = cliforn.dtatual

            if not self.vl_updated or (self.vl_updated <= vl_updated_at):
                self._update_from_cliforn(cliforn)
                self._update_address_from_cliforn(cliforn)
                self._update_phones_from_cliforn(cliforn)

                self.vl_created = cliforn.dtcad
                self.vl_updated = vl_updated_at
                
        except Cliforn.DoesNotExist:
            # Log error or handle as needed
            pass
        except Exception as e:
            # Log unexpected errors
            raise

    def _update_from_cliforn(self, cliforn):
        """Update basic customer data from Cliforn object"""
        self.name = cliforn.nome
        self.company_name = cliforn.razsocial
        self.person_or_company = cliforn.fj
        
        if self.person_or_company == CustomerType.COMPANY:
            self.cnpj = cliforn.cgc
            self.cpf = None
        else:
            self.cnpj = None
            self.cpf = cliforn.cgc

        self.state_registration = cliforn.inscr
        self.municipal_registration = cliforn.codmun
        self.contact_person = cliforn.contato
        self.email = cliforn.email
        self.emailnfe = cliforn.emailnfe

    def _update_address_from_cliforn(self, cliforn):
        """Update customer address from Cliforn object"""
        address, _ = CustomerAddress.objects.get_or_create(customer=self)
        address.update_from_cliforn(cliforn)

    def _update_phones_from_cliforn(self, cliforn):
        """Update customer phone numbers from Cliforn object"""
        phone_numbers = [
            num for num in [cliforn.telres, cliforn.telcom, cliforn.tel2, cliforn.fax]
            if num
        ]

        if phone_numbers:
            self.phone_number = phone_numbers[0]
            
            # Add additional phone numbers
            for phone in phone_numbers[1:]:
                CustomerPhone.objects.get_or_create(
                    customer=self,
                    phone_number=phone
                )

    def save(self, *args, **kwargs):
        """Save the customer instance"""
        if not self.id:
            self.slug = slugify_uniquely(self.name, self.__class__)
        
        if not self.short_name:
            self.short_name = self.name[:60]

        self.clean()
        self.sync_with_vialogos()
        super().save(*args, **kwargs)


class CustomerAddress(models.Model):
    """Customer address information"""
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='address'
    )

    street = models.CharField(_('Street'), max_length=120)
    number = models.CharField(_('Number'), max_length=10, blank=True, null=True)
    complement = models.CharField(_('Complement'), max_length=120, blank=True, null=True)
    district = models.CharField(_('District'), max_length=120, blank=True, null=True)
    city = models.CharField(_('City'), max_length=120, blank=True, null=True)
    state = models.CharField(
        _('State'),
        max_length=2,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}$',
                message=_('Enter a valid state code (e.g., SP)')
            )
        ]
    )
    zip_code = models.CharField(
        _('Zip Code'),
        max_length=9,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{5}-\d{3}$',
                message=_('Enter a valid ZIP code in XXXXX-XXX format')
            )
        ]
    )

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Customer Address')
        verbose_name_plural = _('Customer Addresses')
        indexes = [
            models.Index(fields=['city', 'state'])
        ]

    def __str__(self):
        return self.get_full_address()

    def get_full_address(self):
        """Return formatted full address"""
        parts = [self.street]
        if self.number:
            parts.append(self.number)
        if self.complement:
            parts.append(self.complement)
        if self.district:
            parts.append(self.district)
        if self.city and self.state:
            parts.append(f'{self.city} - {self.state}')
        if self.zip_code:
            parts.append(f'CEP: {self.zip_code}')
        return ', '.join(filter(None, parts))

    def update_from_cliforn(self, cliforn):
        """Update address from Cliforn object"""
        self.street = cliforn.endereco
        self.number = cliforn.num
        self.district = cliforn.bairro
        self.city = cliforn.cidade
        self.state = cliforn.estado
        self.zip_code = cliforn.cep
        self.complement = cliforn.complemento
        self.save()


class CustomerPhone(models.Model):
    """Additional customer phone numbers"""
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='phones'
    )

    phone_number = models.CharField(
        _('Phone'),
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=_('Enter a valid phone number')
            )
        ]
    )
    description = models.CharField(
        _('Description'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_('e.g., Work, Home, Mobile')
    )

    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        verbose_name = _('Customer Phone')
        verbose_name_plural = _('Customer Phones')
        ordering = ['customer', 'phone_number']
        unique_together = ['customer', 'phone_number']

    def __str__(self):
        if self.description:
            return f'{self.phone_number} ({self.description})'
        return self.phone_number