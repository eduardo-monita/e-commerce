from django.contrib import admin
from catalogs.models import Catalog


# Register your models here.
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "image", "created_at", "updated_at", "is_active"]
    list_display_links = ["name"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    filter_horizontal = ["products"]
    fieldsets = [
        [None, {
            "fields": ["name", "description", "image", "alt_image", "products"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["name"]
    list_per_page = 12
    ordering = ["name"]
