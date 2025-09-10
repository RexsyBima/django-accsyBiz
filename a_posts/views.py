from django.http import HttpRequest
from vote.models import UP, DOWN
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
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
        # TODO: handle if the post_feature got more than 3 upvotes
        # # vote, created = PostFeatureVote.objects.get_or_create(post_feature=post_feature, user=request.user)
        # if created:
        #     vote.value = value
        #     vote.save()
        # else:
        #     vote.value = value
        #     vote.save()
        #     messages.success(request, 'Vote updated successfully.')
        return redirect('place_detail', pk=pk)
    return redirect('place_detail', pk=pk)
