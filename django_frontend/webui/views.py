from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .forms import BikeForm

def index(request):
    return render(request, "index.html")

def bike_list(request):
    url = f"{settings.API_BASE_URL}/api/bikes/"
    response = requests.get(url, cookies=request.COOKIES)
    bikes = response.json() if response.status_code == 200 else []
    return render(request, "bikes.html", {"bikes": bikes})

def add_bike(request):
    if request.method == "POST":
        form = BikeForm(request.POST)
        if form.is_valid():
            url = f"{settings.API_BASE_URL}/api/bikes/"
            requests.post(url, json=form.cleaned_data, cookies=request.COOKIES)
            return redirect("bike_list")
    else:
        form = BikeForm()
    return render(request, "add_bike.html", {"form": form})

def edit_bike(request, bike_id):
    url = f"{settings.API_BASE_URL}/api/bikes/{bike_id}/"
    if request.method == "POST":
        form = BikeForm(request.POST)
        if form.is_valid():
            requests.put(url, json=form.cleaned_data, cookies=request.COOKIES)
            return redirect("bike_list")
    else:
        response = requests.get(url, cookies=request.COOKIES)
        if response.status_code == 200:
            form = BikeForm(initial=response.json())
        else:
            return redirect("bike_list")
    return render(request, "edit_bike.html", {"form": form, "bike_id": bike_id})

def delete_bike(request, bike_id):
    url = f"{settings.API_BASE_URL}/api/bikes/{bike_id}/"
    requests.delete(url, cookies=request.COOKIES)
    return redirect("bike_list")
