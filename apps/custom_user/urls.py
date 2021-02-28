from django.contrib import admin
from django.urls import path, include
from apps.custom_user.views import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

urlpatterns = [
    path('auth/', auth)
]
