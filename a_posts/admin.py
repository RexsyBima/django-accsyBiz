from django.contrib import admin
from .models import PostFeature, CommentPlace,PostFeatureVote

# Register your models here.
admin.site.register(PostFeature)
admin.site.register(CommentPlace)
admin.site.register(PostFeatureVote)
