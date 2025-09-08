from django.views.generic import DetailView 
from .models import Place

# Create your views here.
class PlaceGetDetail(DetailView):
    model = Place
    template_name = 'a_places/detail.html'
    context_object_name = 'place'
