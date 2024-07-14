from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from modules.signups.models import TouristSignup


@admin.register(TouristSignup)
class TouristSignupAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "tour_instance",
                    "tourist",
                    "status",
                    "people_quantity",
                )
            },
        ),
        (
            "Оплата",
            {
                "fields": ("payment", "reserved_till"),
                "classes": ("grp-collapse", "grp-closed"),
            },
        ),
        (
            "Служебная информация",
            {"fields": ("created_date", "modified_date"),
             "classes": ("grp-collapse", "grp-closed")},
        ),
    )

    list_display = (
        "created_date",
        "tour_instance",
        "tourist",
        "status",
        "people_quantity",
        "payment",
        "reserved_till",
    )

    list_filter = (
        "tour_instance",
        "tourist",
        "status",
        ("reserved_till", DateRangeFilter),
        ("created_date", DateRangeFilter),
    )

    readonly_fields = ("tour_instance", "tourist", "people_quantity", "created_date", "modified_date")
    search_fields = ("pk", "tour_instance", "tourist")
