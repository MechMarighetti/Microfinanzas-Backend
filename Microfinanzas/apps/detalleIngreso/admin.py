from django.contrib import admin
from .models import DetalleIngreso

@admin.register(DetalleIngreso)
class DetalleIngresoAdmin(admin.ModelAdmin):
    list_display= ['fecha_creacion','monto_detalle'] 
    search_fields = ['descrpcion', 'producto__nombre', 'servicio__nombre']