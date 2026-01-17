from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("hello/", views.hello, name="hello"),
    path("goodbye/", views.goodbye, name="goodbye"),
]
