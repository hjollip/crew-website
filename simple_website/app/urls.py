
from django.urls import path
from .views import LandingPageView, HelloPageView, GoodbyePageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('hello/', HelloPageView.as_view(), name='hello'),
    path('goodbye/', GoodbyePageView.as_view(), name='goodbye'),
]
