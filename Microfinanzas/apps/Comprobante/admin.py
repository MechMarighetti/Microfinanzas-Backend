from django.contrib import admin
from .models import Comprobante

@admin.register(Comprobante) 
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'fecha', 'tipo', 'medio_pago', 'monto')
    search_fields = ('numero', 'fecha', 'tipo', 'medio_pago')
    list_filter = ('fecha', 'medio_pago', 'tipo')