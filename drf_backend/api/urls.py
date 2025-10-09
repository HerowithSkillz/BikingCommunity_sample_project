from django.urls import path
from . import views, auth_views

urlpatterns = [
    path("auth/csrf/", auth_views.get_csrf_token, name="get_csrf_token"),

    path("bikes/", views.bike_list, name="bike_list"),
    path("bikes/create/", views.bike_create, name="bike_create"),
    path("bikes/<int:pk>/", views.bike_detail, name="bike_detail"),
    path("bikes/<int:pk>/update/", views.bike_update, name="bike_update"),
    path("bikes/<int:pk>/delete/", views.bike_delete, name="bike_delete"),
]