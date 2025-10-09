from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["GET"])
def get_csrf_token(request):
    token = get_token(request)
    return Response({"csrfToken": token})

@csrf_exempt
@api_view(["GET"])
def current_user(request):
    if request.user.is_authenticated:
        return JsonResponse({"id": request.user.id, "username": request.user.username})
    return JsonResponse({"error": "Not logged in"}, status=401)
@csrf_exempt
@api_view(["POST"])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Logged in", "user": {"id": user.id, "username": user.username}})
    return JsonResponse({"error": "Invalid credentials"}, status=400)

@csrf_exempt
@api_view(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({"message": "Logged out"})

@csrf_exempt
@api_view(["POST"])
def register_view(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"}, status=400)

    try:
        validate_password(password)
    except ValidationError as e:
        return JsonResponse({"error": e.messages}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse(
        {"message": "User registered", "user": {"id": user.id, "username": user.username}},
        status=201,
    )
