from django import forms

from .models import PostFeature, CommentPlace
from django_ckeditor_5.widgets import CKEditor5Widget

class PostFeatureForm(forms.ModelForm):
    class Meta:
        model = PostFeature
        fields = ['body', 'feature']
        widgets = {
            'body': CKEditor5Widget(config_name='extends'),
        }


class CommentPlaceForm(forms.ModelForm):
    class Meta:
        model = CommentPlace
        fields = ['body']
        widgets = {
            'body': CKEditor5Widget(config_name='extends'),
        }
