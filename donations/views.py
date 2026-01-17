from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from campaigns.models import Campaign
from registrations.models import Registration
from .models import Donation


@login_required
def donate(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    # User must be registered for the campaign
    registration = get_object_or_404(
        Registration,
        user=request.user,
        campaign=campaign
    )

    # Block ONLY if there is a pending donation
    pending = Donation.objects.filter(
        registration=registration,
        payment_status="P"
    ).first()

    if pending:
        messages.info(
            request,
            "You already have a donation in progress. Please wait for it to complete."
        )
        return redirect("campaign_detail", campaign.id)

    if request.method == "POST":
        amount = request.POST.get("amount")

        if not amount:
            messages.error(request, "Please enter a donation amount.")
            return redirect("donate", campaign_id=campaign.id)

        # Create a new donation attempt
        donation = Donation.objects.create(
            campaign=campaign,
            registration=registration,
            amount=amount,
            payment_status="P",
            payment_provider="sandbox"
        )

        # MOCK payment result (success for now)
        donation.payment_status = "S"
        donation.save()

        return redirect("donation_success", campaign_id=campaign.id)

    return render(request, "donations/donate.html", {
        "campaign": campaign
    })


@login_required
def donation_success(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, "donations/success.html", {
        "campaign": campaign
    })


@login_required
def donation_failed(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    return render(request, "donations/failed.html", {
        "campaign": campaign
    })
