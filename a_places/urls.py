from django.urls import path
from .views import PlaceGetDetail

urlpatterns = [
    path('<int:pk>/', PlaceGetDetail.as_view(), name='place_detail'),
]

