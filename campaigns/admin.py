from django.contrib import admin
from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "goal_amount",
        "start_date",
        "end_date",
        "is_active",
    )

    list_filter = (
        "is_active",
        "start_date",
        "end_date",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (None, {
            "fields": ("title", "description")
        }),
        ("Financial Info", {
            "fields": ("goal_amount",)
        }),
        ("Schedule", {
            "fields": ("start_date", "end_date")
        }),
        ("Status", {
            "fields": ("is_active",)
        }),
        ("Timestamps", {
            "fields": ("created_at",)
        }),
    )
