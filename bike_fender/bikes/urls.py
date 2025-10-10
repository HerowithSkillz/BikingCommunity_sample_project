from rest_framework import routers
from django.urls import path, include
from .views import BikeViewSet

router = routers.DefaultRouter()
router.register(r'bikes', BikeViewSet, basename='bikes')

urlpatterns = [
    path('', include(router.urls)),
]
