from django.shortcuts import render
from campaigns.models import Campaign

def home(request):
    campaigns = Campaign.objects.filter(is_active=True)
    return render(request, "home.html", {
        "campaigns": campaigns
    })

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")
