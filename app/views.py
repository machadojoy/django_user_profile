from django.shortcuts import render
from django.views import generic
from .task import add
from .forms import CustomUserCreateForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "home.html"


class CreateProfile(generic.CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreateForm
    success_url = '/login'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request, "Account was created for " + form.cleaned_data["first_name"]
                             + " " + form.cleaned_data["last_name"])
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


    '''def form_valid(self, form):
        form.save()
        return super(CreateProfile, self).form_valid(form)'''


class LoginView(generic.FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request=self.request, message="Invalid credentials")
        else:
            login(self.request, user)
            messages.success(self.request, "You are logged in")
            return redirect(self.success_url)


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect('/')