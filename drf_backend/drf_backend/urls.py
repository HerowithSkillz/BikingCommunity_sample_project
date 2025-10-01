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
from rest_framework.routers import DefaultRouter
from api.views import BikeViewSet
from api import auth_views

router = DefaultRouter()
router.register(r"api", BikeViewSet, basename="API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),

    #auth end points
    path("api/auth/register/", auth_views.register_view),
    path("api/auth/login/", auth_views.login_view),
    path("api/auth/logout/", auth_views.logout_view),
    path("api/auth/user/", auth_views.current_user_view),
]
