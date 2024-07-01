from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from modules.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    # "tourist_signup__user",
                    # "tourist_signup__tour",
                    "channel",
                    "amount",
                )
            },
        ),
        (
            "Чек",
            {
                "fields": ("info",),
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
        # "tourist_signup__user",
        # "tourist_signup__tour_instance",
        "channel",
        "amount",
        "info",
        "created_date",
        "modified_date",
    )

    list_filter = (
        # "tourist_signup__user",
        "tourist_signup__tour_instance",
        "tourist_signup__tour_instance__tour",
        ("created_date", DateRangeFilter)
    )

    readonly_fields = ("info", "created_date", "modified_date")
    search_fields = ("pk", "tourist_signup__user")
