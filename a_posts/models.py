from django.db import models
from a_features.models import Feature
from a_places.models import Place
from django.contrib.auth.models import User

# Create your models here.
class PostFeature(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_features')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: add new body field with ckeditor
    # body 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('place', 'feature', 'user')

    def __str__(self):
        return f"{self.place.name} - {self.feature.code} by {self.user.username}"


