from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from voidpaste.models import Category, Paste, Comment, User


@admin.register(User)
class UserAdmin(BaseUserAdmin): ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin): ...


@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "category", "created_at", "delete_at", "link")
    date_hierarchy = "created_at"
    list_display_links = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): ...


admin.site.unregister(Group)
