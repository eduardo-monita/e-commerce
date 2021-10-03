from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import TimestampModel
from posts.models import Post
from products.models import Category


# Create your models here.
class Banner(TimestampModel):
    link = models.URLField(
        verbose_name=_("Link"),
        max_length=255,
        db_index=True,
        help_text=_("Link to page of some product.")
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="managements/banner"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")

    def __str__(self) -> str:
        return self.link


class Promotion(TimestampModel):
    link = models.URLField(
        verbose_name=_("Link"),
        max_length=255,
        db_index=True,
        help_text=_("Link to Promotion.")
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="managements/promotion"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )

    class Meta:
        verbose_name = _("Promotion")
        verbose_name_plural = _("Promotions")

    def __str__(self) -> str:
        return self.link


class Home(TimestampModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )
    subtitle = models.CharField(
        verbose_name=_("Subtitle"),
        max_length=255,
    )
    most_acessed = models.BooleanField(
        verbose_name=_("Most acessed"),
        default=True,
        help_text=_("Most acessed is active?")
    )
    most_sold = models.BooleanField(
        verbose_name=_("Most sold"),
        default=True,
        help_text=_("Most sold is active?")
    )
    most_favorite = models.BooleanField(
        verbose_name=_("Most favorite"),
        default=True,
        help_text=_("Most favorite is active?")
    )
    banners = models.ManyToManyField(
        verbose_name=_("Banners"),
        to=Banner,
        related_name="home",
        help_text=_("Banners that will show in home.")
    )
    categories = models.ManyToManyField(
        verbose_name=_("Categories"),
        to=Category,
        related_name="home",
        help_text=_("Categories that will show in home.")
    )
    promotions = models.ManyToManyField(
        verbose_name=_("Promotions"),
        to=Promotion,
        related_name="home",
        help_text=_("Promotions that will show in home.")
    )
    posts = models.ManyToManyField(
        verbose_name=_("Posts"),
        to=Post,
        related_name="home",
        help_text=_("Posts that will show in home.")
    )

    class Meta:
        verbose_name = _("Home")
        verbose_name_plural = _("Main Page")

    def __str__(self) -> str:
        return self.title
