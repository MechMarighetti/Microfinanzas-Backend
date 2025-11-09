from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import LoginView, LogoutView, CreateView
from .models import Usuario

class CustomLoginView(LoginView):
    template_name = 'usuario/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    model= Usuario
    template_name = 'usuario/register.html'
    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "dni",
            "phone",
            "address",
            "password1",
            "password2",
        ]