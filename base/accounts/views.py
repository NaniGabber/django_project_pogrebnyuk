from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = "Registration confirmation"
            message = render_to_string(
                "accounts/activation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            send_mail(subject, message, "admin@mysite.com", [user.email])
            print("EMAIL SENT TO:", user.email)
            print("MESSAGE:", message)

            messages.info(request, "We've send a confirmation list to your email")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated! Now, you can login")
        return redirect("login")
    else:
        messages.error(request, "Invalid or expired activation link.")
        return redirect("register")


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile,
            initial={"password": ""}
        )

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "accounts/profile.html", {
        "u_form": u_form,
        "p_form": p_form,
    })
