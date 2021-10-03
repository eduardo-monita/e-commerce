from django.contrib import admin
from managements.models import Banner, Promotion, Home


# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["link", "image", "created_at", "updated_at", "is_active"]
    list_display_links = ["link"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["link", "image", "alt_image"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["link"]
    list_per_page = 12
    ordering = ["link"]


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ["link", "image", "created_at", "updated_at", "is_active"]
    list_display_links = ["link"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["link", "image", "alt_image"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["link"]
    list_per_page = 12
    ordering = ["link"]


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ["title", "subtitle", "created_at", "updated_at", "is_active"]
    list_display_links = ["title"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    filter_horizontal = ["banners", "categories", "promotions", "posts"]
    fieldsets = [
        [None, {
            "fields": ["title", "subtitle", "banners", "categories", "promotions", "posts"]
        }],
        ['Advanced options', {
            "classes": ["collapse"],
            "fields": ["most_acessed", "most_sold", "most_favorite"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["title", "subtitle"]
    list_per_page = 12
    ordering = ["title"]

    def has_add_permission(self, request, obj=None):
        if Home.objects.count() >= 1:
            return False
        return True
