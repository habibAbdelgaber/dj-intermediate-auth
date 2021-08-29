from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .models import Profile
from .forms import UserRegistrationForm, ProfileForm

# USER VIEWS
def home(request):
    return render(request, 'home.html')


def detail(request):
    profile = Profile.objects.all()
    update_profile = Profile.objects.get()
    form = ProfileForm(request.POST)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, instance=update_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'You have updated your profile!')
            return redirect('detail')
    elif request.method == "GET":
        form = ProfileForm(request.POST or None, instance=update_profile)

    # context = {'form': form}
    context = {
        'profile': profile,
        'update_profile': update_profile,
        'form': form
        }
    return render(request, 'accounts/detail.html', context)


# def update(request, pk):
#     profile = Profile.objects.get(id=pk)
#     form = ProfileForm(request.POST, instance=profile)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST or None, instance=profile)
#         if form.is_valid():
#             user_profile = form.save(commit=False)
#             user_profile.user = request.user
#             user_profile.save()
#             messages.success(request, 'You have updated your profile!')
#             return redirect('detail')
#     elif request.method == "GET":
#         form = ProfileForm(
#             instance=profile)

#     context = {'form': form}
#     return render(request, 'accounts/detail.html', context)


# AUTHENTICATION
def signup(request):
    # form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('/')
    else:
        form = UserRegistrationForm(request.POST)

    # form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


# Custom password change view(logic)
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('/')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'accounts/password_change.html', context)
    
