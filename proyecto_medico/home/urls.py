# URLS Parameters del modulo home
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]

# URLS Parameters del modulo sessiones