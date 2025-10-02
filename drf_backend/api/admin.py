from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'owner', 'created_at', 'updated_at')
    list_filter = ('brand', 'owner')
    search_fields = ('name', 'brand', 'owner__username')
