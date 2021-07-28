from django.forms import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

UserProfileFormset = inlineformset_factory(User, UserProfile, fields=('username', 'first_name', 'last_name',
                                                                      'password1', 'password2'))