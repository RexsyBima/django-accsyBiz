from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from a_features.models import Feature
from a_places.models import Place
from django.contrib.auth.models import User

# Create your models here.
class PostFeature(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_features')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('place', 'feature', 'user')

    def __str__(self):
        return f"{self.place.name} - {self.feature.code} by {self.user.username}"


class CommentPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.place.name} - {self.feature.code} by {self.user.username}" # pyright: ignore[reportAttributeAccessIssue]
