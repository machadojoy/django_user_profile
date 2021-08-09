from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.forms import ModelForm

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


class EditUserProfileForm(ModelForm):
    first_name = forms.CharField(max_length=256, required=False)
    last_name = forms.CharField(max_length=256, required=False)
    #username = forms.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            #self.fields['username'].initial = self.instance.user.username
        except User.DoesNotExist:
            pass

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user',]

    def save(self, commit=True):
        profile = super(EditUserProfileForm, self).save(commit=False)
        user = profile.user
        user.first_name = self.cleaned_data.get('first_name', None)
        user.last_name = self.cleaned_data.get('last_name', None)
        user.save()
        profile.save()
        return profile

UserProfileFormset = inlineformset_factory(User, UserProfile, fields=('location',))