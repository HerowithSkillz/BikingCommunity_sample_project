from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Bike(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(default="No description provided")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bikes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"
