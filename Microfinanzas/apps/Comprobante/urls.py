from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('crear/', views.crear_comprobante, name='crear_comprobante'),
    path('detalle/<int:comprobante_id>/', views.detalle_comprobante, name='detalle_comprobante'),
]