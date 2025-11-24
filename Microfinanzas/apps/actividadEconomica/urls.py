from django.urls import path
from .views import *

urlpatterns = [
    # URLs para Categoria
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    #path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    #path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    # URLs para Servicio
    path('servicios/', ServicioListView.as_view(), name='servicio_list'),
    path('servicios/crear/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicios/<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
    #path('servicios/<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),
    #path('servicios/<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),
    
    # URLs para Producto
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    #path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    #path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),
]