from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LogoutView

class LogoutViewCustom(LogoutView):
    next_page = '/'  # Redirect to home page after logout


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after signup
            auth_login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('/')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'a_users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                # Redirect to next page or home page
                return redirect('/')  # Redirect to home page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'a_users/login.html', {'form': form})

@login_required(login_url='/users/login/')
def profile_view(request):
    return render(request, 'a_users/profile.html')
