from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.html import mark_safe
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import (
    Cart,
    ProductCart,
    UserFavorite,
    UserShopped,
    UserAccessed,
    ProductUserAccessed
)
User = get_user_model()


class UserFavoriteInline(admin.TabularInline):
    model = UserFavorite
    filter_horizontal = ["products"]
    fields = ["products"]
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False


class UserShoppedInline(admin.TabularInline):
    model = UserShopped
    filter_horizontal = ["products"]
    fields = ["products"]
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False


@ admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = [
        "email", "first_name", "last_name", "phone", "date_of_birth", "is_staff",  "is_superuser", "is_active"
    ]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    filter_horizontal = ["groups", "user_permissions"]
    readonly_fields = ["view_cart", "view_products_accessed", "last_login", "date_joined", "created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["email", "password"]
        }],
        ["Personal info", {
            "fields": ["first_name", "last_name", "phone", "date_of_birth", "picture", "alt_picture"]
        }],
        ["Permissions", {
            "fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"]
        }],
        ["Relations", {
            "fields": ["view_cart", "view_products_accessed"]
        }],
        ["Important dates", {
            "classes": ["collapse"],
            "fields": ["last_login", "date_joined", "created_at", "updated_at"]
        }]
    ]
    add_fieldsets = [
        [None, {
            "classes": ["wide"],
            "fields": ["email", "password1", "password2"]
        }]
    ]
    search_fields = ["email", "first_name", "last_name", "phone"]
    list_per_page = 12
    ordering = ["email"]
    inlines = [UserFavoriteInline, UserShoppedInline]

    def view_cart(self, instance):
        if hasattr(instance, "cart") and instance.cart:
            return mark_safe(
                f"<a href='{reverse('admin:accounts_cart_change', args=[instance.cart.id])}'>{instance.cart}</a>"
            )
        return mark_safe(
            f"<a href='{reverse('admin:accounts_cart_add', args=[])}'>Add a cart</a>"
        )
    view_cart.short_description = "Cart Link"

    def view_products_accessed(self, instance):
        if hasattr(instance, "accessed") and instance.accessed:
            return mark_safe(
                f"""
                <a href='{reverse('admin:accounts_useraccessed_change', args=[instance.accessed.id])}'>
                    {instance.accessed}
                </a>
                """
            )
        return mark_safe(
            f"<a href='{reverse('admin:accounts_useraccessed_add', args=[])}'>Add a products a access</a>"
        )
    view_products_accessed.short_description = "Products Accessed Link"


class ProductCartInline(admin.TabularInline):
    model = ProductCart
    readonly_fields = ["sum_freight", "sum_price"]
    autocomplete_fields = ["product"]
    fields = ["product", "quantity", "freight", "sum_freight", "sum_price"]
    extra = 0


@ admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "total_freight", "subtotal", "total", "created_at", "updated_at", "is_active"]
    list_display_links = ["user"]
    list_filter = ["is_active"]
    readonly_fields = ["total_freight", "subtotal", "total", "created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["user", "destination_zip_code", "total_freight", "subtotal", "total"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["user"]
    list_per_page = 12
    ordering = ["user"]
    inlines = [ProductCartInline]

    def has_delete_permission(self, request, obj=None):
        return False


class ProductUserAccessedInline(admin.TabularInline):
    model = ProductUserAccessed
    readonly_fields = ["hit"]
    autocomplete_fields = ["product"]
    fields = ["product", "hit"]
    extra = 0


@admin.register(UserAccessed)
class UserAccessedAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "updated_at", "is_active"]
    list_display_links = ["user"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["user"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["user"]
    list_per_page = 12
    ordering = ["user"]
    inlines = [ProductUserAccessedInline]

    def has_delete_permission(self, request, obj=None):
        return False
