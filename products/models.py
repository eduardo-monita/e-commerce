from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import TimestampModel


# Create your models here.
class Category(TimestampModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        db_index=True
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="products/category"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name


class Product(TimestampModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=9,
        decimal_places=2
    )
    freight = models.DecimalField(
        verbose_name=_("Freight"),
        max_digits=9,
        decimal_places=2,
        default=0,
        help_text=_("Cost of freight.")
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="products/product"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )
    categories = models.ManyToManyField(
        verbose_name=_("Categories"),
        to=Category,
        related_name="products"
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return self.name


class Access(TimestampModel):
    product = models.OneToOneField(
        verbose_name=_("Product"),
        to=Product,
        related_name="access",
        on_delete=models.CASCADE
    )
    hit = models.PositiveIntegerField(
        verbose_name=_("Hit"),
        default=0,
        help_text=_("Number of access.")
    )

    class Meta:
        verbose_name = _("Access")
        verbose_name_plural = _("Accesses")

    def __str__(self) -> str:
        return f"{self.product.name} - {self.hit}"


class Sale(TimestampModel):
    product = models.OneToOneField(
        verbose_name=_("Product"),
        to=Product,
        related_name="sale",
        on_delete=models.CASCADE
    )
    hit = models.PositiveIntegerField(
        verbose_name=_("Hit"),
        default=0,
        help_text=_("Number of sales.")
    )

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")

    def __str__(self) -> str:
        return f"{self.product.name} - {self.hit}"


class Characteristic(TimestampModel):
    product = models.ForeignKey(
        verbose_name=_("Product"),
        to=Product,
        related_name=_("characteristics"),
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        help_text=_("Ex: Color, widht, volts ...")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Description related to name of characteristic.")
    )

    class Meta:
        verbose_name = _("Characteristic")
        verbose_name_plural = _("Characteristics")

    def __str__(self) -> str:
        return self.name
