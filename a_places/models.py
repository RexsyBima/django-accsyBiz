from enum import unique
from django.db import models
from a_features.models import Feature

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)  # from DOING BUSINESS AS NAME
    business_category = models.CharField(max_length=200)  # from DOING BUSINESS AS NAME
    legal_name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, default="Chicago")
    state = models.CharField(max_length=20, default="IL")
    zip_code = models.CharField(max_length=15, blank=True)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    community_area_name = models.CharField(max_length=100, blank=True)

    category = models.CharField(max_length=100, blank=True)  # from LICENSE DESCRIPTION
    license_status = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.latitude} {self.longitude}"

class PlaceFeature(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='features')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('place', 'feature')

    def __str__(self):
        return f"{self.place.name} - {self.feature.code}"
