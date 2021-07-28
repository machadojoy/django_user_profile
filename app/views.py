from django.shortcuts import render
from django.views import generic
from .task import add

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "home.html"
