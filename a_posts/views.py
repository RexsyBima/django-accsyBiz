from django.http import HttpRequest, HttpResponseBadRequest
from django.views.generic import ListView
from vote.models import UP, DOWN
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from a_places.models import Place, PlaceFeature
from django.shortcuts import get_object_or_404, redirect, render
from a_posts.models import PostFeature, CommentPlace
from .forms import PostFeatureForm, CommentPlaceForm
from django.shortcuts import render

# Create your views here.
#
class PostFeatureListView(ListView):
    model = PostFeature
    template_name = 'a_posts/postfeature_list.html'
    context_object_name = 'post_features'
    paginate_by = 10

    def get_queryset(self):
        return PostFeature.objects.select_related('user', 'place').order_by('-created_at')

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
    place = Place.objects.get(pk=pk)
    context = {
        'form': form,
        'place': place,
        'detail' : 'Submit Comment'
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
    place = Place.objects.get(pk=pk)
    context = {
        'form': form,
        'place': place,
        'detail' : 'Submit Feature'
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
