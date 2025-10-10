from rest_framework import serializers
from .models import Bike


class BikeSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    
    class Meta:
        model = Bike
        fields = ['id', 'model', 'company', 'year', 'description', 'owner', 'owner_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'owner_username', 'created_at', 'updated_at']
