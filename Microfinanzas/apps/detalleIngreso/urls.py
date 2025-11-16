from django.urls import path
from .views import DetalleIngresoCreate, DetalleIngresoLista


urlpatterns = [
    path('', DetalleIngresoLista.as_view(), name='detalleIngresoList'),
    path('', DetalleIngresoCreate.as_view(), name='crear_detIngreso')
] 

