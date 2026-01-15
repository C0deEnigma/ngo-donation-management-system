from django.urls import path
from . import views

urlpatterns = [
    path("campaigns/", views.campaign_list, name="campaign-list"),
    path("campaigns/<int:pk>/", views.campaign_detail, name="campaign-detail"),
    path("campaigns/<int:pk>/register/", views.campaign_register, name="campaign-register"),
]

