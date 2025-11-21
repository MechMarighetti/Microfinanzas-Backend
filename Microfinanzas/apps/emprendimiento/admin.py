from django.contrib import admin
from .models import Emprendimiento

@admin.register(Emprendimiento)
class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'fecha_creacion')
    search_fields = ('nombre', 'usuario__username', 'descripcion')
