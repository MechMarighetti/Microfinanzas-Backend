from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Transaccion
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ..mixins import PreviousPageMixin


class TransaccionCreateView(LoginRequiredMixin, PreviousPageMixin, CreateView):
    model = Transaccion
    template_name = 'transaccion_form.html'
    fields = ['fecha','importe', 'descripcion','tipoTrx', 'comprobante_id','emprendimiento_id'] 
    success_url = reverse_lazy('transaccion_list')

class TransaccionListView(LoginRequiredMixin, ListView):
    model = Transaccion
    template_name = 'transaccion_list.html'
    context_object_name = 'transaccion'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar ingresos por el usuario logueado
        return queryset.filter(emprendimiento_id__usuario=self.request.user)
        #return queryset lista completa de trx
    
class TransaccionDetailView(LoginRequiredMixin, PreviousPageMixin, DetailView):
    model = Transaccion
    template_name = 'transaccion_detail.html'
    context_object_name = 'transaccion'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        # Asegurar que solo pueda ver ingresos de sus emprendimientos
        return super().get_queryset().filter(emprendimiento_id__usuario=self.request.user)