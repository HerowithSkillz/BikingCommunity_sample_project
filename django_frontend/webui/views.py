import requests
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

API_BASE_URL = settings.API_BASE_URL  
# Helper: get user info from backend
def get_logged_in_user(request):
    cookies = {"sessionid": request.COOKIES.get("sessionid")}
    r = requests.get(f"{API_BASE_URL}/api/auth/user/", cookies=cookies)
    if r.status_code == 200:
        return r.json()
    return None

def index(request):
    # If user is authenticated, show bike list
    if request.user.is_authenticated:

        return render(request, 'index.html')
    else:
        # redirect to login page
        return redirect('login')

# ----------------------
# Auth Views
# ----------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        r = requests.post(
            f"{API_BASE_URL}/api/auth/login/",
            json={"username": username, "password": password},
            cookies=request.COOKIES
        )

        if r.status_code == 200:
            response = redirect("bike_list")
            # Forward backend sessionid to frontend
            if "sessionid" in r.cookies:
                response.set_cookie("sessionid", r.cookies.get("sessionid"))
            return response
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        r = requests.post(
            f"{API_BASE_URL}/api/auth/signup/",
            json={"username": username, "password": password}
        )

        if r.status_code == 201:
            messages.success(request, "Registration successful! Please login.")
            return redirect("login")
        else:
            messages.error(request, "Registration failed. Try another username.")

    return render(request, "register.html")


def logout_view(request):
    cookies = {"sessionid": request.COOKIES.get("sessionid")}
    r = requests.post(f"{API_BASE_URL}/api/auth/logout/", cookies=cookies)

    response = redirect("login")
    response.delete_cookie("sessionid")
    messages.info(request, "Logged out successfully.")
    return response

# ----------------------
# Bike CRUD Views
# ----------------------

def bike_list(request):
    user = get_logged_in_user(request)
    if not user:
        return redirect("login")

    cookies = {"sessionid": request.COOKIES.get("sessionid")}
    r = requests.get(f"{API_BASE_URL}/bikes/", cookies=cookies)
    bikes = r.json() if r.status_code == 200 else []

    return render(request, "bikes.html", {"bikes": bikes, "user": user})


def add_bike(request):
    user = get_logged_in_user(request)
    if not user:
        return redirect("login")

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description"),
            "manufacturer": request.POST.get("manufacturer"),
        }
        cookies = {"sessionid": request.COOKIES.get("sessionid")}
        r = requests.post(f"{API_BASE_URL}/bikes/", json=data, cookies=cookies)
        if r.status_code == 201:
            return redirect("bike_list")
        else:
            messages.error(request, "Failed to add bike.")

    return render(request, "add_bike.html", {"user": user})


def edit_bike(request, bike_id):
    user = get_logged_in_user(request)
    if not user:
        return redirect("login")

    cookies = {"sessionid": request.COOKIES.get("sessionid")}

    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "description": request.POST.get("description"),
            "manufacturer": request.POST.get("manufacturer"),
        }
        r = requests.put(f"{API_BASE_URL}/bikes/{bike_id}/", json=data, cookies=cookies)
        if r.status_code in [200, 204]:
            return redirect("bike_list")
        else:
            messages.error(request, "Failed to update bike.")

    # GET: fetch bike info
    r = requests.get(f"{API_BASE_URL}/bikes/{bike_id}/", cookies=cookies)
    bike = r.json() if r.status_code == 200 else {}
    return render(request, "edit_bike.html", {"bike": bike, "user": user})


def delete_bike(request, bike_id):
    user = get_logged_in_user(request)
    if not user:
        return redirect("login")

    cookies = {"sessionid": request.COOKIES.get("sessionid")}
    r = requests.delete(f"{API_BASE_URL}/bikes/{bike_id}/", cookies=cookies)
    return redirect("bike_list")
