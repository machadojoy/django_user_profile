from django.shortcuts import render
from django.views import generic
from .task import add
from .forms import CustomUserCreateForm
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "home.html"


class CreateProfile(generic.CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreateForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(CreateProfile, self).form_valid(form)