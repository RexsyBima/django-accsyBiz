from django.shortcuts import render
from typing import Any
from django.db.models import Prefetch
from django.views.generic import TemplateView
from a_places.models import Place, PlaceFeature

# Create your views here.

# class A_Pages:
#     class Home(TemplateView):
#         template_name = 'a_pages/home.html'


class Home(TemplateView):
    template_name = 'a_pages/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Get places with their features using select_related for better performance
        places = Place.objects.prefetch_related('features__feature')
        
        # Convert to list of dictionaries with feature information
        place_data = []
        for place in places:
            features = place.get_features()
            feature_labels = [pf.feature.label for pf in features] if features else []
            
            place_data.append({
                'id': place.id,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'name': place.name,
                'category': place.category,
                'feature_labels': feature_labels,
            })
        
        context['places'] = place_data
        return context
