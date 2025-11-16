from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from .models import DetalleIngreso
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView): 
    model = DetalleIngreso
    template_name = 'index.html'
    context_object_name = 'detalleIngresos'
    
    def get_queryset(self):
        queryset = DetalleIngreso.objects.all()

        # BÚSQUEDA EXACTA
        fecha_busqueda = self.request.GET.get("fecha")

        # RANGO
        fecha_desde = self.request.GET.get("desde")
        fecha_hasta = self.request.GET.get("hasta")

        # FILTRO: fecha exacta
        if fecha_busqueda:
            queryset = queryset.filter(fecha=fecha_busqueda)

        # FILTRO: desde
        if fecha_desde:
            queryset = queryset.filter(fecha__gte=fecha_desde)

        # FILTRO: hasta
        if fecha_hasta:
            queryset = queryset.filter(fecha__lte=fecha_hasta)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ultimoDetalleIngreso'] = DetalleIngreso.objects.last()

        # Mantener valores del formulario
        context['fecha_busqueda'] = self.request.GET.get("fecha", "")
        context['desde'] = self.request.GET.get("desde", "")
        context['hasta'] = self.request.GET.get("hasta", "")

        return context
