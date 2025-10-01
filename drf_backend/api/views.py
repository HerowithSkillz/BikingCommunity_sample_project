from rest_framework import viewsets, permissions
from .models import Bike
from .serializers import BikeSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all().order_by('-created_at')
    serializer_class = BikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_permissions(self):
        #Only authenticated users can C/U/D 
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()] 