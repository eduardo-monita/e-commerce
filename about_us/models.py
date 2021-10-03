from django.db import models
from helpers.models import TimestampModel
from django.utils.translation import ugettext_lazy as _


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
        max_length=255
    )
    cnpj = models.CharField(
        verbose_name=_("CNPJ"),
        unique=True,
        db_index=True,
        max_length=255
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
