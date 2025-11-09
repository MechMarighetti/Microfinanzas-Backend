from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username',  'dni', 'email', 'miembroActivo')
    search_fields = ('username', 'dni', 'email')
    list_filter = ('is_active', 'is_staff')