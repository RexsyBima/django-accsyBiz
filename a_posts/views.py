from django.http import HttpRequest
from django.contrib import messages
from a_places.models import Place
from django.shortcuts import get_object_or_404, redirect, render
from a_posts.models import PostFeature, CommentPlace
from .forms import PostFeatureForm, CommentPlaceForm
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.

def comment_form(request: HttpRequest, pk):
    if request.method == 'POST':
        data = CommentPlaceForm(request.POST)
        data.instance.user = request.user
        data.instance.place = get_object_or_404(Place, pk=pk)
        if data.is_valid():
            obj = data.save(commit=True)
            messages.success(request, 'Your comment has been posted successfully.')
            return redirect('place_detail', pk=pk)
    form = CommentPlaceForm()
    context = {
        'form': form,
    }
    return render(request, 'a_posts/feature_form.html', context)

def feature_form(request : HttpRequest, pk):
    if request.method == 'POST':
        data = PostFeatureForm(request.POST)
        data.instance.user = request.user
        data.instance.place = get_object_or_404(Place, pk=pk)
        if data.is_valid():
            obj = data.save(commit=True)
            messages.success(request, 'Your feature has been posted successfully.')
            return redirect('place_detail', pk=pk)
    form = PostFeatureForm()
    context = {
        'form': form,
    }
    return render(request, 'a_posts/feature_form.html', context)
