from __future__ import unicode_literals
from products.models import Product

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from accounts.managers import UserManager
from helpers.models import TimestampModel


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email address'),
        unique=True,
        db_index=True,
        help_text=_("Email used to login in the plataform and admin dashboard")
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=30,
        blank=True,
        null=True,
        db_index=True
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=30,
        blank=True,
        null=True,
        db_index=True
    )
    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=50,
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(
        verbose_name=_('Date of birth'),
        blank=True,
        null=True
    )
    picture = models.ImageField(
        verbose_name=_('Picture'),
        upload_to='accounts/user/',
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
        verbose_name=_('Active'),
        default=True,
        help_text=_("The user is active?")
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff status'),
        default=False,
        help_text=_("The user can access the admin dashboard?")
    )
    is_superuser = models.BooleanField(
        verbose_name=_('Superuser status'),
        default=False,
        help_text=_("The user can be a superuser?")
    )
    last_login = models.DateTimeField(
        verbose_name=_('Last login'),
        blank=True,
        null=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Cart(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("cart"),
        on_delete=models.CASCADE
    )
    freight = models.DecimalField(
        verbose_name=_("Freight"),
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=_("Cost of freight.")
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        through="ProductCart",
        related_name="cart"
    )

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")

    def __str__(self) -> str:
        return f'Cart({self.id}): {self.user.email}'

    @property
    def subtotal(self):
        """This function will return total value without shipping"""
        subtotal = 0
        for product_cart in self.products_cart.all():
            subtotal += product_cart.product.price
        return subtotal

    @property
    def total(self):
        """This function will return the subtotal plus freight value."""
        return self.subtotal() + float(self.freight)


class ProductCart(TimestampModel):
    product = models.ForeignKey(
        verbose_name=_("Product"),
        to=Product,
        related_name="cart_products",
        on_delete=models.PROTECT
    )
    cart = models.ForeignKey(
        verbose_name=_("Cart"),
        to=Cart,
        related_name="products_cart",
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
        default=0,
    )

    class Meta:
        verbose_name = _("Product Cart")
        verbose_name_plural = _("Products Cart")

    def __str__(self) -> str:
        return f'{self.product} - {self.cart}'

    @property
    def total_value(self):
        """This function will return the total value, the product multiple quantity"""
        return self.product.price * self.quantity


class ProductFavorite(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("favorite"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        related_name="user_favorite"
    )

    class Meta:
        verbose_name = _("Product Favorite")
        verbose_name_plural = _("Products Favorite")

    def __str__(self) -> str:
        return f'{self.user} - {self.products}'


class ProductShopped(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("shopped"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        related_name="user_shopped"
    )

    class Meta:
        verbose_name = _("Product Shopped")
        verbose_name_plural = _("Products Shopped")

    def __str__(self) -> str:
        return f'{self.user} - {self.products}'


class ProductAccessed(TimestampModel):
    user = models.OneToOneField(
        verbose_name=_("User"),
        to=User,
        related_name=_("accessed"),
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        verbose_name=_("Products"),
        to=Product,
        related_name="user_accessed"
    )

    class Meta:
        verbose_name = _("Product Accessed")
        verbose_name_plural = _("Products Accessed")

    def __str__(self) -> str:
        return f'{self.user} - {self.products}'
