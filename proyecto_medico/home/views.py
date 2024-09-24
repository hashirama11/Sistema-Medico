from django.shortcuts import render
from django.http import HttpResponse, HttpRequest # Estos modulos son para pruebas

# Create your views here.

def home(request):
    return render(request, "home/index.html", {})
