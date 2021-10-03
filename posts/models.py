from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from helpers.models import TimestampModel
from ckeditor.fields import RichTextField


# Create your models here.
class Author(TimestampModel):
    email = models.EmailField(
        verbose_name=_("Email address"),
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=255,
    )
    picture = models.ImageField(
        verbose_name=_("Picture"),
        upload_to="posts/author/",
    )
    alt_picture = models.CharField(
        verbose_name=_("Alt picture"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the picture.")
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        return f'{self.first_name} {self.last_name}'.strip()


class Post(TimestampModel):
    author = models.ForeignKey(
        verbose_name=_("Athor"),
        to=Author,
        related_name=_("posts"),
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255
    )
    subtitle = models.CharField(
        verbose_name=_("SubTitle"),
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
