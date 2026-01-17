from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from campaigns.models import Campaign
from .models import Registration


@login_required
def register_for_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    # Check if already registered
    existing = Registration.objects.filter(
        user=request.user,
        campaign=campaign
    ).first()

    if existing:
        messages.info(request, "You are already registered for this campaign.")
        return redirect("campaign_detail", campaign.id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()

        Registration.objects.create(
            user=request.user,
            campaign=campaign,
            name=name
        )

        messages.success(request, "Registration successful.")
        return redirect("campaign_detail", campaign.id)

    context = {
        "campaign": campaign
    }
    return render(request, "registrations/register.html", context)
