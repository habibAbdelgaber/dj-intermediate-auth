from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Your Username', 'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your e-mail', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirm', 'class': 'form-control'}))
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def set_password(self):
        created = self.cleaned_data
        if created['password2'] != created['password1']:
            raise forms.ValidationError('Passwords do not match!')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['short_intro', 'bio_content', 'country', 'city', 'date_joined']