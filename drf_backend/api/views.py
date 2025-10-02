from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Bike
from .serializers import BikeSerializer


# --------------------
# LIST + CREATE
# --------------------
@api_view(["GET"])
@permission_classes([AllowAny])  # anyone can view bikes
def bike_list(request):
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # only logged-in users can create
def bike_create(request):
    serializer = BikeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)  # attach logged-in user as owner
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --------------------
# DETAIL + UPDATE + DELETE
# --------------------
@api_view(["GET"])
@permission_classes([AllowAny])
def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    serializer = BikeSerializer(bike)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def bike_update(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    if bike.owner != request.user:
        return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)

    serializer = BikeSerializer(bike, data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def bike_delete(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    if bike.owner != request.user:
        return Response({"error": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)

    bike.delete()
    return Response({"message": "Bike deleted"}, status=status.HTTP_204_NO_CONTENT)

