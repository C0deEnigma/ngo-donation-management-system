from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from registrations.models import Registration
from donations.models import Donation

def post_login_redirect(user):
    if user.is_staff:
        return redirect('/admin/')
    return redirect('profile')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return post_login_redirect(user)
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    user = request.user

    registrations = (
        Registration.objects
        .filter(user=user)
        .select_related('campaign')
        .order_by('-created_at')
    )

    donations = (
        Donation.objects
        .filter(registration__user=user)
        .select_related('registration', 'registration__campaign')
        .order_by('-created_at')
    )

    return render(
        request,
        "accounts/profile.html",
        {
            "user_obj": user,
            "registrations": registrations,
            "donations": donations,
        }
    )
