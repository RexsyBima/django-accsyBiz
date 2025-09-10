from django.http import HttpRequest, HttpResponseBadRequest
from vote.models import UP, DOWN
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from a_places.models import Place, PlaceFeature
from django.shortcuts import get_object_or_404, redirect, render
from a_posts.models import PostFeature, CommentPlace
from .forms import PostFeatureForm, CommentPlaceForm
from django.shortcuts import render

# Create your views here.

@login_required
def comment_form(request: HttpRequest, pk):
    if request.method == 'POST':
        data = CommentPlaceForm(request.POST)
        data.instance.user = request.user
        data.instance.place = get_object_or_404(Place, pk=pk)
        if data.is_valid():
            data.save(commit=True)
            messages.success(request, 'Your comment has been posted successfully.')
            return redirect('place_detail', pk=pk)
    form = CommentPlaceForm()
    context = {
        'form': form,
    }
    return render(request, 'a_posts/feature_form.html', context)

@login_required
def feature_form(request : HttpRequest, pk):
    if request.method == 'POST':
        data = PostFeatureForm(request.POST)
        data.instance.user = request.user
        data.instance.place = get_object_or_404(Place, pk=pk)
        if data.is_valid():
            data.save(commit=True)
            messages.success(request, 'Your feature has been posted successfully.')
            return redirect('place_detail', pk=pk)
    form = PostFeatureForm()
    context = {
        'form': form,
    }
    return render(request, 'a_posts/feature_form.html', context)

@login_required
def vote(request: HttpRequest, pk):
    if request.method == 'POST':
        post_feature = get_object_or_404(PostFeature, id=request.GET.get("feature_id"))
        match request.POST.get('vote'):
            case 'downvote':
                if post_feature.votes.exists(request.user.id, action=DOWN): # pyright: ignore[reportAttributeAccessIssue]
                    messages.error(request, 'You have already downvoted this feature.')
                    return redirect('place_detail', pk=pk)
                messages.success(request, 'Downvote success')
                post_feature.votes.down(request.user.id) # pyright: ignore[reportAttributeAccessIssue]
            case 'upvote':
                if post_feature.votes.exists(request.user.id, action=UP): # pyright: ignore[reportAttributeAccessIssue]
                    messages.error(request, 'You have already upvoted this feature.')
                    return redirect('place_detail', pk=pk)
                post_feature.votes.up(request.user.id) # pyright: ignore[reportAttributeAccessIssue]
                messages.success(request, 'Upvote success')
        if post_feature.votes.count() >= 2:
            _, create = PlaceFeature.objects.get_or_create(place=post_feature.place,feature=post_feature.feature,)
            if create:
                messages.success(request, f'This feature has been added to the place features list!')
        return redirect('place_detail', pk=pk)
    return redirect('place_detail', pk=pk)

@login_required
def delete_comment(request : HttpRequest, pk):
    if request.method == 'POST':
        CommentPlace.objects.get(id=pk,user=request.user).delete()
        messages.success(request, 'Comment has been successfully deleted')
        return redirect('place_detail', pk=request.GET.get("placeid"))
    return HttpResponseBadRequest("Bad Request")
