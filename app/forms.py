from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

class CustomUserCreateForm(UserCreationForm):
    location = forms.CharField()
    birthday = forms.DateField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

UserProfileFormset = inlineformset_factory(User, UserProfile, fields=('location',))