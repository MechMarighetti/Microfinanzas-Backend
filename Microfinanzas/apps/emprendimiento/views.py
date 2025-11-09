from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .models import Emprendimiento
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class EmprendimientoCreateView(LoginRequiredMixin, CreateView):
    model = Emprendimiento
    template_name = 'emprendimiento_form.html'
    fields = ['nombre', 'descripcion', 'usuario']
    success_url = reverse_lazy('emprendimiento_list')

    def form_valid(self, form):
        messages.success(self.request, 'Emprendimiento creado exitosamente.')
        return super().form_valid(form)
    
class EmprendimientoListView(LoginRequiredMixin, ListView):
    model = Emprendimiento
    template_name = 'emprendimiento_list.html'
    context_object_name = 'emprendimientos'
    paginate_by = 10

    def get_queryset(self):
        return Emprendimiento.objects.filter(usuario=self.request.user).order_by('nombre')

class EmprendimientoDetailView(LoginRequiredMixin, DetailView):
    model = Emprendimiento
    template_name = 'emprendimiento_detail.html'