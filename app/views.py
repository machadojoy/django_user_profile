from django.shortcuts import render
from django.views import generic
from .task import add
from .forms import CustomUserCreateForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "home.html"


class CreateProfile(generic.CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreateForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = CustomUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})

    '''def form_valid(self, form):
        form.save()
        return super(CreateProfile, self).form_valid(form)'''