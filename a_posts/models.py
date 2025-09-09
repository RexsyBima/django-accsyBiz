from django.db import models
from django.db.models import Sum
from django.utils.safestring import mark_safe
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


    def total_votes(self):
        return self.votes.aggregate(total=Sum('value'))['total'] or 0 # pyright: ignore[reportAttributeAccessIssue]

    def body_data(self):
        return mark_safe(self.body)

    def __str__(self):
        return f"{self.place.name} - {self.feature.code} by {self.user.username}"

class PostFeatureVote(models.Model):
    UP = 1
    NEUTRAL = 0
    DOWN = -1
    VALUE_CHOICES = ((UP, 'Upvote'), (NEUTRAL, 'Neutral'), (DOWN,'Downvote'))

    post_feature = models.ForeignKey(PostFeature, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.SmallIntegerField(default=0, choices=VALUE_CHOICES)
    

    class Meta:
        unique_together = ('post_feature', 'user')

    def __str__(self):
        return f"Vote by {self.user.username} on {self.post_feature}" # pyright: ignore[reportAttributeAccessIssue]



class CommentPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = CKEditor5Field('Text', config_name='extends', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.place.name} - by {self.user.username}" # pyright: ignore[reportAttributeAccessIssue]

