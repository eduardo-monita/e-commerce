from django.db import models
from django.utils.translation import ugettext_lazy as _
from helpers.models import TimestampModel
from ckeditor.fields import RichTextField


# Create your models here.
class Post(TimestampModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="posts/post"
    )
    alt_image = models.CharField(
        verbose_name=_("Alt image"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the image.")
    )
    highlight = models.BooleanField(
        verbose_name=_("Highlight"),
        default=False,
        help_text=_("This post is a highlight? Note: Will show the three last created posts.")
    )
    summary = models.CharField(
        verbose_name=_("Summary"),
        max_length=510,
        help_text=_("This field is to show in the lists, a summary of post.")
    )
    body = RichTextField(
        verbose_name=_("Body"),
        help_text=_("Body of post, save in html format.")
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self) -> str:
        return self.title
