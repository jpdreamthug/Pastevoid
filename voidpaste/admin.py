from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from voidpaste.models import Category, Paste, Comment, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "category",
        "created_at",
        "delete_at",
        "link"
    )
    date_hierarchy = "created_at"
    list_display_links = ("title",)
    search_fields = ("title",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


admin.site.register(Comment)


admin.site.unregister(Group)
