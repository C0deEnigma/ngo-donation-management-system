from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "registration_name",
        "registration_user",
        "registration_campaign",
        "amount",
        "payment_status",
        "payment_provider",
        "transaction_id",
        "created_at",
    )

    list_filter = (
        "payment_provider",
        "payment_status",
        "created_at",
    )

    search_fields = (
        "registration__name",
        "registration__user__username",
        "registration__user__email",
        "transaction_id",
    )

    raw_id_fields = (
        "registration",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "registration",
        "amount",
        "payment_status",
        "payment_provider",
        "transaction_id",
        "created_at",
    )

    fieldsets = (
        ("Payment Info", {
            "fields": (
                "amount",
                "payment_status",
                "payment_provider",
                "transaction_id",
            )
        }),
        ("Registration Info", {
            "fields": ("registration",)
        }),
        ("Timestamps", {
            "fields": ("created_at",)
        }),
    )

    # ---------- display helpers ----------

    def registration_name(self, obj):
        return obj.registration.name
    registration_name.short_description = "Name"

    def registration_user(self, obj):
        return obj.registration.user
    registration_user.short_description = "User"

    def registration_campaign(self, obj):
        return obj.registration.campaign
    registration_campaign.short_description = "Campaign"
