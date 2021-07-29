from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

class CustomUserCreateForm(UserCreationForm):
    location = forms.CharField()
    birthday = forms.DateField()
    image = forms.FileField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data.get('password1')
        user.set_password(password)
        user.location = self.cleaned_data.get('location')
        user.birthday = self.cleaned_data.get('birthday')
        user.image = self.cleaned_data.get('image')
        user.save()
        return user

UserProfileFormset = inlineformset_factory(User, UserProfile, fields=('location',))