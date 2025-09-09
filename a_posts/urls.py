from django import urls
from django.urls import URLPattern, path
from . import views 

urlpatterns = [
    path('comment/<int:pk>/', views.comment_form, name='comment_form'),
    path('feature/<int:pk>/', views.feature_form, name='feature_form'),
]
