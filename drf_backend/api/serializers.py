from rest_framework import serializers
from .models import Bike
from django.contrib.auth import get_user_model

User = get_user_model()

class BikeSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source="owner.username", read_only=True)
    class Meta:
        model = Bike
        fields =  ["id", "owner", "owner_username", "name", "brand", "price","created_at"]
        read_only_fields = ["id", "owner", "owner_username", "created_at"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
