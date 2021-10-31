from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from accounts.managers import UserManager
from helpers.models import TimestampModel
from products.models import Product


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email address"),
        unique=True,
        db_index=True,
        help_text=_("Email used to login in the plataform and admin dashboard")
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=30,
        blank=True,
        null=True,
        db_index=True
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=30,
        blank=True,
        null=True,
        db_index=True
    )
    phone = models.CharField(
        verbose_name=_("Phone number"),
        max_length=255,
        help_text=_("Format example: (999) 99999-9999, (99) 9999-9999"),
        validators=[
            RegexValidator(regex="^\(\d{2,3}\) \d{4,5}\-\d{4}$", message="Invalid phone number", code="invalid_phone")
        ]
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of birth"),
        blank=True,
        null=True
    )
    picture = models.ImageField(
        verbose_name=_("Picture"),
        upload_to="accounts/user/",
        blank=True,
        null=True,
        help_text=_("Profile picture")
    )
    alt_picture = models.CharField(
        verbose_name=_("Alt picture"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The text that represents the picture.")
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_("The user is active?")
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_("The user can access the admin dashboard?")
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superuser status"),
        default=False,
        help_text=_("The user can be a superuser?")
    )
    last_login = models.DateTimeField(
        verbose_name=_("Last login"),
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Date joined"),
        default=timezone.now
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this User."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Cart(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("cart"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        through="ProductCart",
        related_name="cart"
    )
    destination_zip_code = models.CharField(
        verbose_name=_("Origin zip code"),
        max_length=9,
        help_text=_("Format example: 99999-999"),
        validators=[
            RegexValidator(regex="^\d{5}\-\d{3}$", message="Invalid origin zip code", code="invalid_origin_zip_code")
        ]
    )

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self) -> str:
        if self.user.first_name:
            return f"{self.user.first_name}'s cart"
        return f"{self.user.email}"

    @property
    def total_freight(self):
        """This function will return total freight"""
        freight = 0
        for product_cart in self.products_cart.all():
            freight += product_cart.calc_freight()
        return f"{round(freight, 2):.2f}"

    @property
    def subtotal(self):
        """This function will return total value without freight"""
        subtotal = 0
        for product_cart in self.products_cart.all():
            subtotal += product_cart.price()
        return f"{round(subtotal, 2):.2f}"

    @property
    def total(self):
        """This function will return the subtotal plus freight value."""
        subtotal = 0
        freight = 0
        for product_cart in self.products_cart.all():
            subtotal += product_cart.price()
            freight += product_cart.calc_freight()
        return f"{round(subtotal + freight, 2):.2f}"


class ProductCart(TimestampModel):
    product = models.ForeignKey(
        verbose_name=_("Product"),
        to=Product,
        related_name="cart_products",
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        verbose_name=_("Cart"),
        to=Cart,
        related_name="products_cart",
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=0,
    )
    freight = models.DecimalField(
        verbose_name=_("Freight"),
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Cost of freight.")
    )

    class Meta:
        verbose_name = _("Product Cart")
        verbose_name_plural = _("Products Cart")

    def __str__(self) -> str:
        return f"{self.product} - {self.cart}"

    @property
    def sum_freight(self):
        return f"{round(self.calc_freight(), 2):.2f}"

    @property
    def sum_price(self):
        return f"{round(self.price(), 2):.2f}"

    def calc_freight(self):
        """This function will return the total freight, the product freight multiple quantity"""
        if self.freight and self.quantity:
            return self.freight * self.quantity
        return 0

    def price(self):
        """This function will return the total price, the product price multiple quantity"""
        if hasattr(self, 'product') and self.product and self.product.price:
            return self.product.price * self.quantity
        return 0


class UserFavorite(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("favorite"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        related_name="user_favorite",
        blank=True
    )

    class Meta:
        verbose_name = _("Product Favorite")
        verbose_name_plural = _("Products Favorite")

    def __str__(self) -> str:
        return f"{self.user} - {self.products}"


class UserShopped(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("shopped"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        related_name="user_shopped",
        blank=True
    )

    class Meta:
        verbose_name = _("Product Shopped")
        verbose_name_plural = _("Products Shopped")

    def __str__(self) -> str:
        return f"{self.user} - {self.products}"


class UserAccessed(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("accessed"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        through="ProductUserAccessed",
        related_name="user_accessed",
        blank=True
    )

    class Meta:
        verbose_name = _("Product Accessed")
        verbose_name_plural = _("Products Accessed")

    def __str__(self) -> str:
        if self.user.first_name:
            return f"{self.user.first_name}'s access"
        return f"{self.user.email}"


class ProductUserAccessed(models.Model):
    user_accessed = models.ForeignKey(
        verbose_name=_("Cart"),
        to=UserAccessed,
        related_name="product_user_accessed",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        verbose_name=_("Product"),
        to=Product,
        related_name="user_accessed_product",
        on_delete=models.CASCADE
    )
    hit = models.PositiveIntegerField(
        verbose_name=_("Hit"),
        default=0,
        help_text=_("Number of access.")
    )

    class Meta:
        verbose_name = _("Product User Accessed")
        verbose_name_plural = _("Products User Accessed")

    def __str__(self) -> str:
        return f"{self.product} - {self.user_accessed}"
