from django.contrib import admin
from .models import Transaccion

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'monto', 'fecha', 'usuario')
    search_fields = ('tipo', 'usuario__username')
    list_filter = ('tipo', 'fecha')