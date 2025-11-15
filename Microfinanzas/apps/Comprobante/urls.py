from django.urls import path
from .views import CrearComprobanteView, DetalleComprobanteView, IndexView

urlpatterns = [
    path('home', IndexView.as_view(), name='index'),
    path('/', CrearComprobanteView.as_view(), name='crear_comprobante'),
    path('detalle/<int:comprobante_id>/', DetalleComprobanteView.as_view(), name='detalle_comprobante'),
] 