from django.urls import  path
from . import views 

urlpatterns = [
    path('comment/<int:pk>/', views.comment_form, name='comment_form'),
    path('feature/<int:pk>/', views.feature_form, name='feature_form'),
    path('vote/<int:pk>/', views.vote, name='handle_vote'),
    path('delete/comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('index/', views.PostFeatureListView.as_view(), name='PostFeatureListView'),
]
