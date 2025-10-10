from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'bikes', views.BikeViewSet)

urlpatterns = router.urls
