from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Bike
        fields = ["id", "name", "brand", "description", "owner", "created_at", "updated_at"]
        read_only_fields = ["owner", "created_at", "updated_at"]

