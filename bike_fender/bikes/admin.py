from django.contrib import admin
from .models import Bike


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('company', 'model', 'year', 'created_at')
    search_fields = ('company', 'model')
    list_filter = ('year',)
