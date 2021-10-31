from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe
from products.models import (
    Category,
    Package,
    Product,
    Access,
    Sale,
    Characteristic
)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "created_at", "updated_at", "is_active"]
    list_display_links = ["name"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["name", "image", "alt_image"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["name"]
    list_per_page = 12
    ordering = ["name"]


class CharacteristicInline(admin.StackedInline):
    model = Characteristic
    fields = ["name", "description"]
    extra = 0


class PackageInline(admin.StackedInline):
    model = Package
    fields = ["format", "weight", "length", "width", "height"]
    extra = 0


@ admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at", "is_active"]
    list_display_links = ["name"]
    list_filter = ["is_active"]
    readonly_fields = ["count_access", "count_sales", "created_at", "updated_at"]
    filter_horizontal = ["categories"]
    fieldsets = [
        [None, {
            "fields": ["name", "description", "price", "image", "alt_image", "categories"]
        }],
        ["Data", {
            "classes": ["collapse"],
            "fields": ["count_access", "count_sales"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }],
    ]
    search_fields = ["name"]
    list_per_page = 12
    ordering = ["name"]
    inlines = [CharacteristicInline, PackageInline]

    def count_access(self, instance):
        if hasattr(instance, "access") and instance.access:
            return instance.access.hit
        return 0
    count_access.short_description = "Numbers of access"

    def count_sales(self, instance):
        if hasattr(instance, "sale") and instance.sale:
            return instance.sale.hit
        return 0
    count_sales.short_description = "Number of sales"


@ admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ["product", "hit", "created_at", "updated_at", "is_active"]
    list_display_links = ["product", "hit"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["product"]
    fieldsets = [
        [None, {
            "fields": ["product", "hit"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["product"]
    list_per_page = 12
    ordering = ["hit", "product"]


@ admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["product", "hit", "created_at", "updated_at", "is_active"]
    list_display_links = ["product", "hit"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["product"]
    fieldsets = [
        [None, {
            "fields": ["product", "hit"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["product"]
    list_per_page = 12
    ordering = ["hit", "product"]
