from typing import Any
from django.views.generic import DetailView 
from .models import Place

# Create your views here.
class PlaceGetDetail(DetailView):
    model = Place
    template_name = 'a_places/detail.html'
    context_object_name = 'place'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['features'] = context['place'].features.all()
        context['features_posts'] = context['place'].post_features.all()
        context['comments'] = context['place'].post_comments.all()
        return  context
