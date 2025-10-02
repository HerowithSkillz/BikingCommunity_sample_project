"""
URL configuration for django_frontend project.

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
from django.urls import path
from webui import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.bike_list, name="index"),

    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    #Bikes
    path("bikes/", views.bike_list, name="bike_list"),
    path("bikes/add/", views.add_bike, name="add_bike"),
    path("bikes/<int:bike_id>/edit/", views.edit_bike, name="edit_bike"),
    path("bikes/<int:bike_id>/delete/", views.delete_bike, name="delete_bike"),
]

