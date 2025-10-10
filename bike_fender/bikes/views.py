from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Bike
from .serializers import BikeSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 50


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all().order_by('-created_at')
    serializer_class = BikeSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
