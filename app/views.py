from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "app/home.html")

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def hello(request):
    return render(request, "app/hello.html")
