from django.contrib import admin
from .models import Servicio, Producto, Categoria

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ( 'categoria', 'emprendimiento')
    search_fields = ( 'descripcion', 'categoria__nombre')
    list_filter = ('categoria',)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'emprendimiento')
    search_fields =  ('descripcion', 'categoria__nombre')
    list_filter = ('categoria',)
