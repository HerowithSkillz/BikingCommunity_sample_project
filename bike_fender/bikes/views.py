from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied
from .models import Bike
from .serializers import BikeSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 50


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all().order_by('-created_at')
    serializer_class = BikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        """Automatically set the owner to the current user when creating a bike."""
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """Only allow users to update their own bikes."""
        bike = self.get_object()
        if bike.owner != self.request.user:
            raise PermissionDenied("You can only edit your own bikes.")
        serializer.save()

    def perform_destroy(self, instance):
        """Only allow users to delete their own bikes."""
        if instance.owner != self.request.user:
            raise PermissionDenied("You can only delete your own bikes.")
        instance.delete()
