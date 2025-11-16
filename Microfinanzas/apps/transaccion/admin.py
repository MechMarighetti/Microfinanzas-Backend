from django.contrib import admin
from .models import Ingreso, Egreso

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'importe', 'fecha')
    search_fields = ('id', 'fecha', 'descripcion', 'comprobante__numero')
    list_filter = ('id', 'fecha')

@admin.register(Egreso)
class EgresoAdmin(admin.ModelAdmin):
    list_display = ('id', 'importe', 'fecha')
    search_fields = ('id', 'fecha', 'descripcion', 'comprobante__numero')
    list_filter = ('id', 'fecha')