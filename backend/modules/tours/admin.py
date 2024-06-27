from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from modules.tours.models import Tour


class LocationInline(admin.TabularInline):
    model = Tour.locations.through


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "price",
                    "complexity",
                    "program",
                )
            },
        ),
        (
            "Расписание",
            {
                "fields": ("schedule", "is_active"),
                "classes": ("grp-collapse", "grp-closed"),
            },
        ),
        (
            "Служебная информация",
            {"fields": ("created_date", "modified_date"),
             "classes": ("grp-collapse", "grp-closed")},
        ),
    )
    inlines = [
        LocationInline,
    ]
    list_display = (
        "name",
        "description",
        "price",
        "complexity",
        "program",
        "schedule",
        "is_active",
        "created_date",
        "modified_date",
    )

    list_filter = (
        "complexity",
        "locations",
        ("created_date", DateRangeFilter)
    )

    readonly_fields = ("created_date", "modified_date")
    search_fields = ("pk", "name")
