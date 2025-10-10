from django.db import models


class Bike(models.Model):
    model = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.company} {self.model} ({self.year})"
