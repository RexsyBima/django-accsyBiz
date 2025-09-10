from django.db import models
from django.db.models import Sum
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field
from a_features.models import Feature
from a_places.models import Place
from vote.models import VoteModel
from django.contrib.auth.models import User

# Create your models here.
class PostFeature(VoteModel, models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_features')
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('place', 'feature', 'user')



    def body_data(self):
        return mark_safe(self.body)

    def __str__(self):
        return f"{self.place.name} - {self.feature.code} by {self.user.username}"




class CommentPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.place.name} - by {self.user.username}" # pyright: ignore[reportAttributeAccessIssue]

