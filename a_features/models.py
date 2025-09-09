from django.db import models

# Create your models here.
class Feature(models.Model):
    code = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.label} ({self.code})"
