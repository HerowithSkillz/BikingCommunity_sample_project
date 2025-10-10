import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

AUTH_SERVER = 'http://127.0.0.1:8001' #URL OF bike_fender

def register_user(request):
    if request.method == 'POST':
        data = {
            "username": request.POST["username"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "password2": request.POST["password2"]
        }
        response = requests.post(f'{AUTH_SERVER}/api/accounts/register/', json=data)
        if response.status_code == 201:
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login_user')
        else:
            messages.error(request, f"Error: {response.json()}")
    return render(request, "register.html")
    
def login_user(request):
    if request.method == 'POST':
        data = {
            "username": request.POST["username"],
            "password": request.POST["password"]
        }
        response = requests.post(f"{AUTH_SERVER}/api/accounts/login/", json=data)
        if response.status_code == 200:
            tokens = response.json()
            #Save JWT tokens in session
            request.session['access'] = tokens['access']
            request.session['refresh'] = tokens['refresh']
            request.session['username'] = data['username']
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, "login.html")
    
def logout_user(request):
    request.session.flush()
    return redirect('login_user')

def dashboard(request):
    access_token = request.session.get('access')
    if not access_token:
        return redirect('login_user')
    
    #Optionally, call protected API endpoint
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(f"{AUTH_SERVER}/api/protected/", headers=headers)
    data = r.json() if r.status_code == 200 else {}

    # Render the community landing page but with the logged-in navbar
    return render(request, 'biker_hub.html', {"user": request.session.get("username"), "data": data})


def home(request):
    """Public landing page for the biker hub.

    If the user is already logged in (session contains 'username'), the
    template will display the logged-in navbar with logout.
    """
    username = request.session.get('username')
    return render(request, 'biker_hub.html', {"user": username})


def bikes_view(request):
    """Render the bikes listing page which fetches bikes from the API client-side."""
    username = request.session.get('username')
    return render(request, 'bikes.html', {"user": username})
