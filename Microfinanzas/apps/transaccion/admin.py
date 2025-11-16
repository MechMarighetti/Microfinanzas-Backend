from django.contrib import admin
from .models import Transaccion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'importe', 'fecha')
    search_fields = ('id', 'fecha', 'descripcion', 'comprobante__numero')
    list_filter = ('id', 'fecha')
