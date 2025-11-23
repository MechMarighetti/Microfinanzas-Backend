from django.urls import path
from .views import EmprendimientoCreateView, EmprendimientoListView, EmprendimientoDetailView
from django.urls import include

urlpatterns = [
    path('', EmprendimientoListView.as_view(), name='emprendimiento_list'),
    path('crear/', EmprendimientoCreateView.as_view(), name='emprendimiento_create'),
    path('<int:pk>/', EmprendimientoDetailView.as_view(), name='emprendimiento_detail'),
    path('trx/', include('apps.transaccion.urls')),
]