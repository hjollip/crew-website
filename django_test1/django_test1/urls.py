from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('logout/', views.logout_view, name='logout'),
]
