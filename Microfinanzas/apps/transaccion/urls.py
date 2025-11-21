from django.urls import path
from .views import TransaccionCreateView, TransaccionListView, TransaccionDetailView

urlpatterns = [
    path('', TransaccionListView.as_view(), name='transaccion_list'),
    path('crear/', TransaccionCreateView.as_view(), name='transaccion_create'),
    path('<int:id>/', TransaccionDetailView.as_view(), name='transaccion_details'),
]