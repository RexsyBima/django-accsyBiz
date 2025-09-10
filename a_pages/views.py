from django.shortcuts import render
from typing import Any
from django.views.generic import TemplateView
from a_places.models import Place

# Create your views here.

# class A_Pages:
#     class Home(TemplateView):
#         template_name = 'a_pages/home.html'


class Home(TemplateView):
    template_name = 'a_pages/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['places'] = list(Place.objects.values('id','latitude', 'longitude', 'name', 'category', 'features__feature__label'))
        for place in context['places']:
            print(place if place['id'] == 1784 else "")
        return context
