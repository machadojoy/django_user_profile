
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('signup/', views.CreateProfile.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('edit/<int:pk>', views.EditView.as_view(), name="edit")
    #path('edit/<slug:slug>', views.EditView.as_view())
]