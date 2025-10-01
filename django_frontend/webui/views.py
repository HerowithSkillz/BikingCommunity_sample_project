from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def bikes_page(request):
    return render(request, "bikes.html")

def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")