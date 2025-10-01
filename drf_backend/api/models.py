from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Bike(models.Model):
    owner = models.ForeignKey(User, related_name="bikes", on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    brand = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"
