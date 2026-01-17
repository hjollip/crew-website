from __future__ import annotations

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def landing(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.POST.get("action") == "logout":
            logout(request)
            return redirect("landing")

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("chatbot")
            messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AuthenticationForm(request)

    return render(request, "core/landing.html", {"form": form})


@login_required
def chatbot(request: HttpRequest) -> HttpResponse:
    history = request.session.get("chat_history", [])

    if request.method == "POST":
        action = (request.POST.get("action") or "").strip()
        if action == "clear":
            request.session.pop("chat_history", None)
            return redirect("chatbot")

        msg = (request.POST.get("message") or "").strip()
        if msg:
            history.append({"role": "user", "text": msg})
            history.append({"role": "bot", "text": "Say what?"})
            history = history[-20:]
            request.session["chat_history"] = history
        return redirect("chatbot")

    return render(request, "core/chatbot.html", {"history": history})


def logout_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        logout(request)
    return redirect("landing")
