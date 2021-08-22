from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'home.html')


def signup(request):
    form = UserRegistrationForm()
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

    form = UserRegistrationForm()
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
    
