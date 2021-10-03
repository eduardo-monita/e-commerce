from django.contrib import admin
from about_us.models import Company, Contact

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["title", "cnpj", "email", "created_at", "updated_at", "is_active"]
    list_display_links = ["title", "cnpj"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["title", "image", "alt_image", "description", "motivation", "principles"]
        }],
        ["Contact", {
            "fields": ["address", "email", "phone", "cnpj"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["title", "cnpj", "email"]
    list_per_page = 12
    ordering = ["title"]

    def has_add_permission(self, request, obj=None):
        if Company.objects.count() >= 1:
            return False
        return True


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "created_at", "updated_at", "is_active"]
    list_display_links = ["name", "email"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["name", "email", "phone", "body"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["name", "email", "phone"]
    list_per_page = 12
    ordering = ["name"]
