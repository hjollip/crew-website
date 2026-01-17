
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class LandingPageView(View):
    def get(self, request):
        return render(request, 'landing.html')
    def post(self, request):
        # Handle login and registration logic
        pass

class HelloPageView(View):
    def get(self, request):
        return render(request, 'hello.html')

class GoodbyePageView(View):
    def get(self, request):
        return render(request, 'goodbye.html')
