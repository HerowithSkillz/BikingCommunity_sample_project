"""
URL configuration for drf_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("api/auth/login/", auth_views.login_view, name="api_login"),
    path("api/auth/logout/", auth_views.logout_view, name="api_logout"),
    path("api/auth/signup/", auth_views.register_view, name="api_signup"),
    path("api/auth/user/", auth_views.current_user, name="api_user"),

    # Bikes API
    path("api/", include("api.urls")),  # include bikes urls
]
