from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from helpers.models import TimestampModel
from localflavor.br.models import BRCNPJField


# Create your models here.
class Company(TimestampModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        help_text=_("Company name or slogan.")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        max_length=255,
        help_text=_("Description telling more about the company.")
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="about_us/company"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=255
    )
    email = models.EmailField(
        verbose_name=_("Email address")
    )
    phone = models.CharField(
        verbose_name=_("Phone number"),
        max_length=255,
        help_text=_("Format example: (999) 99999-9999, (99) 9999-9999"),
        validators=[
            RegexValidator(regex="^\(\d{2,3}\) \d{4,5}\-\d{4}$", message="Invalid phone number", code="invalid_phone")
        ]
    )
    cnpj = BRCNPJField(
        verbose_name=_("CNPJ"),
        help_text=_("Format example: 99.999.999/9999-99"),
        unique=True,
        db_index=True,
        max_length=255
    )
    origin_zip_code = models.CharField(
        verbose_name=_("Origin zip code"),
        max_length=9,
        help_text=_("Format example: 99999-999"),
        validators=[
            RegexValidator(regex="^\d{5}\-\d{3}$", message="Invalid origin zip code", code="invalid_origin_zip_code")
        ]
    )
    motivation = models.TextField(
        verbose_name=_("Motivation"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Why did you start the company? And why do you keep working on it every day?")
    )
    principles = models.TextField(
        verbose_name=_("Principles"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Tell more about the principles of the company.")
    )

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self) -> str:
        return self.title


class Contact(TimestampModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        db_index=True
    )
    email = models.EmailField(
        verbose_name=_("Email address"),
        db_index=True
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        max_length=50
    )
    body = models.TextField(
        verbose_name=_("Body"),
        help_text=_("Body of email.")
    )

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self) -> str:
        return self.name
