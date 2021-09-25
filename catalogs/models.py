from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import TimestampModel
from products.models import Product


# Create your models here.
class Catalog(TimestampModel):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
        db_index=True
    )
    description = models.TextField(
        verbose_name=_("Description")
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="catalogs/catalog"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )
    products = models.ManyToManyField(
        verbose_name=("Products"),
        to=Product,
        related_name="catalogs"
    )

    class Meta:
        verbose_name = _("Catolog")
        verbose_name_plural = _("Catalogs")

    def __str__(self) -> str:
        return self.title
