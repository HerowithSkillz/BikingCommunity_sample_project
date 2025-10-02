from django.urls import path
from . import views

urlpatterns = [
    path("", views.bike_list, name="bike_list"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("bikes/", views.bike_list, name="bike_list"),
    path("bikes/add/", views.add_bike, name="add_bike"),
    path("bikes/edit/<int:bike_id>/", views.edit_bike, name="edit_bike"),
    path("bikes/delete/<int:bike_id>/", views.delete_bike, name="delete_bike"),
]
