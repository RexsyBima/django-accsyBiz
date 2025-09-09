from django.http import HttpRequest
from a_places.models import Place
from django.shortcuts import get_object_or_404, render
from a_posts.models import PostFeature, CommentPlace
from .forms import PostFeatureForm
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

def comment_form(request: HttpRequest, pk):
    return render(request, 'a_places/comment_form.html')

def feature_form(request : HttpRequest, pk):
    if request.method == 'POST':
        data = PostFeatureForm(request.POST)
        data.instance.user = request.user
        data.instance.place = get_object_or_404(Place, pk=pk)
        if data.is_valid():
            obj = data.save(commit=True)
    form = PostFeatureForm()
    context = {
        'form': form,
    }
    return render(request, 'a_places/feature_form.html', context)
