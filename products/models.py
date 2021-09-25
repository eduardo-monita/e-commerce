from django.db import models
from helpers.models import TimestampModel
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Category(TimestampModel):
    name = models.CharField(
        max_length=255,
        help_text=_("Category Name.")
    )

    image = models.ImageField(
        upload_to="products/category",
        help_text=_("Category Image.")
    )

    alt_image = models.CharField(
        max_length=255,
        help_text=_("Category Image Description.")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Access(TimestampModel):
    hit = models.IntegerField(
        help_text=_("Hit.")
    )

    class Meta:
        verbose_name = _("Access")
        verbose_name_plural = _("Accesses")


class Sale(TimestampModel):
    hit = models.IntegerField(
        help_text=_("Hit.")
    )

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")



class Product(TimestampModel):
    name = models.CharField(
        max_length=255,
        help_text=_("Product Name.")
    )

    description = models.CharField(
        max_length=255,
        help_text=_("Product Description.")
    )

    price = models.DecimalField(
        help_text=_("Product Price.")
    )

    image = models.ImageField(
        upload_to="products/product",
        help_text=_("Product Image.")
    )

    alt_image = models.CharField(
        max_length=255,
        help_text=_("Product Image Description.")
    )

    categories = models.ManyToManyField(
        Category,
        help_text=_("Product categories.")
    )

    acecesses = models.ManyToManyField(
        Access,
        help_text=_("Product Accesses.")
    )

    sales = models.ManyToManyField(
        Sale,
        help_text=_("Product Sales.")
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")



class Characteristic(TimestampModel):
    name = models.CharField(
        max_length=255,
        help_text=_("Characteristic Name.")
    )

    description = models.CharField(
        max_length=255,
        help_text=_("Characteristic Description.")
    )

    product = models.ManyToManyField(
        Product,
        help_text=_("Characteristic Associate Product.")
    )

    class Meta:
        verbose_name = _("Characteristic")
        verbose_name_plural = _("Characteristics")