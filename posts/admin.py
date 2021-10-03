from django.contrib import admin
from posts.models import Post, Author


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "created_at", "updated_at", "is_active"]
    list_display_links = ["email", "first_name"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        [None, {
            "fields": ["email", "first_name", "last_name", "picture", "alt_picture"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["email", "first_name"]
    list_per_page = 12
    ordering = ["email"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "image", "created_at", "updated_at", "is_active"]
    list_display_links = ["title"]
    list_filter = ["is_active"]
    readonly_fields = ["created_at", "updated_at"]
    autocomplete_fields = ["author"]
    fieldsets = [
        [None, {
            "fields": ["title", "subtitle", "author", "image", "alt_image", "summary", "body"]
        }],
        ["Register data", {
            "classes": ["collapse"],
            "fields": ["is_active", "created_at", "updated_at"]
        }]
    ]
    search_fields = ["title", "author"]
    list_per_page = 12
    ordering = ["title"]
