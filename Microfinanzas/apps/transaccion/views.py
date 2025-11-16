from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Ingreso, Transaccion, TipoTrx
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from ..emprendimiento.models import Emprendimiento

class TrxCreate(LoginRequiredMixin, CreateView):
    model = Transaccion
    template_name = transaccion_form.html
    fields = ['fecha','importe', 'descripcion','tipoTrx', 'comprobante_id','emprendimiento_id']


class NuevoIngreso(LoginRequiredMixin,CreateView):
    model = Ingreso
    template_name = 'ingreso_form.html'
    fields = ['fecha','importe', 'descripcion', 'comprobante_id','emprendimiento_id']
    success_url = reverse_lazy('ingreso_list')
    def form_valid(self, form):
        # Asigna automáticamente el usuario logueado
        form.instance.usuario = self.request.user
        messages.success(self.request, 'Ingreso registrado exitosamente.')
        return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar emprendimientos del usuario actual
        form.fields['emprendimiento_id'].queryset = Emprendimiento.objects.filter(usuario=self.request.user)
        return form


class IngresoListView(LoginRequiredMixin, ListView):
    model = Ingreso
    template_name = 'ingresolist.html'
    context_object_name = 'ingresos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar ingresos por el usuario logueado
        return queryset.filter(emprendimiento_id__usuario=self.request.user)

class IngresoDetailView(LoginRequiredMixin, DetailView):
    model = Ingreso
    template_name = 'ingreso_detail.html'
    context_object_name = 'ingreso'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        # Asegurar que solo pueda ver ingresos de sus emprendimientos
        return super().get_queryset().filter(emprendimiento_id__usuario=self.request.user)