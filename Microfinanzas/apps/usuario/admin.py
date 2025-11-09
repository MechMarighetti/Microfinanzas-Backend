from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'rol', 'dni', 'email', 'miembroActivo')
    search_fields = ('username', 'dni', 'email')
    list_filter = ('rol', 'is_active')