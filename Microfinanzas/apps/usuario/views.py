from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from .models import Usuario

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30)
    last_name = forms.CharField(label="Apellido", max_length=40)
    email = forms.EmailField(label="Correo electrónico", required=True)
    dni = forms.CharField(label="DNI", max_length=20)
    telefono = forms.CharField(label="Teléfono", max_length=20)
    password = forms.PasswordInput()
    cuit = forms.CharField(label="CUIT", max_length=15)

    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "dni",
            "telefono",
            "cuit",
        ]

class RegisterView(CreateView):
    model = Usuario
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.dni = self.cleaned_data["dni"]
        user.cuit = self.cleaned_data["cuit"]
        user.telefono = self.cleaned_data["telefono"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.rol = "owner", "marketing", "finanzas"
        if commit:
            user.save()
        return user