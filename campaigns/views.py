from .models import Campaign
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def campaign_register(request, pk):
    return HttpResponse(f"Register page for campaign {pk}")

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, "campaigns/campaign_list.html", {
        "campaigns": campaigns
    })

def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, "campaigns/campaign_detail.html", {
        "campaign": campaign
    })