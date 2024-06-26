from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rangefilter.filters import DateRangeFilter

from modules.users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "email", "phone",
        "first_name", "last_name",
        "telegram_id",
        "is_staff", "is_active",
        "last_login",
        "created_date",
        "modified_date",
    )
    list_filter = (
        "email",
        "is_staff", "is_active",
        ("last_login", DateRangeFilter),
        ("created_date", DateRangeFilter),
    )
    fieldsets = (
        (
            None,
            {"fields": ("email", "password",
                        "username", "phone", "telegram_id",
                        "first_name", "last_name")},
        ),
        ("Разрешения", {"fields": ("is_staff", "is_active")}),
        ("Служебная информация", {"fields": ("created_date", "modified_date"),
                                  "classes": ("grp-collapse", "grp-closed")}),
    )
    readonly_fields = ("created_date", "modified_date", "telegram_id")

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email",
                       "password1", "password2",
                       "is_staff", "is_active")
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
