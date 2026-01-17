from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, SignupForm


@require_http_methods(["GET", "POST"])
def landing(request):
    """Landing page that supports login, logout, and signup."""
    login_form = LoginForm(request=request, data=None)
    signup_form = SignupForm(data=None)

    if request.method == "POST":
        action = request.POST.get("action", "")

        if action == "login":
            login_form = LoginForm(request=request, data=request.POST)
            if login_form.is_valid():
                auth_login(request, login_form.get_user())
                messages.success(request, "Logged in.")
                return redirect("landing")
            messages.error(request, "Login failed. Check your username/password.")

        elif action == "signup":
            signup_form = SignupForm(data=request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                auth_login(request, user)
                messages.success(request, "Account created and logged in.")
                return redirect("landing")
            messages.error(request, "Signup failed. Please fix the errors below.")

        elif action == "logout":
            auth_logout(request)
            messages.success(request, "Logged out.")
            return redirect("landing")

        else:
            messages.error(request, "Unknown action.")

    return render(
        request,
        "landing.html",
        {
            "login_form": login_form,
            "signup_form": signup_form,
        },
    )


def hello(request):
    return render(request, "hello.html")


def goodbye(request):
    return render(request, "goodbye.html")
