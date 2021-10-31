from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from helpers.models import TimestampModel
from helpers.freight_correios.constants import (
    PACKAGE_OR_BOX,
    ENVELOPE
)


# Variables
FORMAT = [
    (PACKAGE_OR_BOX, _("Packege or Box")),
    (ENVELOPE, _("Envelope"))
]


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


class Package(TimestampModel):

    product = models.OneToOneField(
        verbose_name=_("Product"),
        to=Product,
        related_name=_("package"),
        on_delete=models.CASCADE
    )
    format = models.PositiveSmallIntegerField(
        verbose_name=_("format"),
        choices=FORMAT,
        default=PACKAGE_OR_BOX,
    )
    weight = models.DecimalField(
        verbose_name=_("weight"),
        max_digits=9,
        decimal_places=3,
        default=0,
        help_text=_(
            "Unit of measurement: kilogram(kg). "
            "In case the format is Package or Box the limit of weight is 30kg (SEDEX 10 10kg)."
            "In case the format is Envelope the limit of weight is 1kg. "
        )
    )
    length = models.PositiveIntegerField(
        verbose_name=_("length"),
        default=0,
        help_text=_(
            "Unit of measurement: centimeter(cm). "
            "In case the format is Package or Box the range of length is 15cm <=> 100cm."
            "In case the format is Envelope the range of length is 16cm <=> 60cm. "
        )
    )
    width = models.PositiveIntegerField(
        verbose_name=_("width"),
        default=0,
        help_text=_(
            "Unit of measurement: centimeter(cm). "
            "In case the format is Package or Box the range of weight is 10cm <=> 100cm."
            "In case the format is Envelope the range of width is 11cm <=> 60cm. "
        )
    )
    height = models.PositiveIntegerField(
        verbose_name=_("height"),
        default=0,
        help_text=_(
            "Unit of measurement: centimeter(cm). "
            "In case the format is Package or Box the range of weight is 1cm <=> 100cm."
            "Fill only if the format is Package or Box!"
        )
    )

    class Meta:
        verbose_name = _("Package")
        verbose_name_plural = _("Packages")

    def clean(self):
        super().clean()
        error = {}
        if self.format == PACKAGE_OR_BOX:
            if self.weight > 30:
                error["weight"] = _("Value above the maximum weight allowed!")
            elif self.weight == 0:
                error["weight"] = _("Weight can not be zero!")
            if self.length < 15 or self.length > 100:
                error["length"] = _("Length not compatible with limits!")
            if self.width < 10 or self.width > 100:
                error["width"] = _("Width not compatible with limits!")
            if self.length < 1 or self.length > 100:
                error["height"] = _("Height not compatible with limits!")
        elif self.format == ENVELOPE:
            if self.weight > 1:
                error["weight"] = _("Value above the maximum weight allowed!")
            elif self.weight == 0:
                error["weight"] = _("Weight can not be zero!")
            if self.length < 16 or self.length > 60:
                error["length"] = _("Length not compatible with limits!")
            if self.width < 11 or self.width > 60:
                error["width"] = _("Width not compatible with limits!")

        if error is not {}:
            raise ValidationError(error)

    def __str__(self) -> str:
        return f"{self.id}"
