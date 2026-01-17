from django.urls import path
from . import views

urlpatterns = [
    path("<int:campaign_id>/", views.donate, name="donate"),
    path("<int:campaign_id>/success/", views.donation_success, name="donation_success"),
    path("<int:campaign_id>/failed/", views.donation_failed, name="donation_failed"),
]
