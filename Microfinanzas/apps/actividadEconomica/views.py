from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Servicio, Producto, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from .mixins import EmprendimientoMixin

""" VISTAS DE CATEGORIA """

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'actividadeconomica/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Búsqueda por nombre o descripción
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(nombre__icontains=search_query) |
                Q(descripcion__icontains=search_query)
            )
        return queryset.order_by('nombre')

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'actividadeconomica/categoria_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría creada exitosamente.')
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'actividadeconomica/categoria_form.html'
    fields = ['nombre', 'descripcion']
    success_url = reverse_lazy('categoria_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoría actualizada exitosamente.')
        return super().form_valid(form)

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'actividadeconomica/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Categoría eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)

class CategoriaDetailView(LoginRequiredMixin, DetailView):
    model = Categoria
    template_name = 'actividadeconomica/categoria_detail.html'
    context_object_name = 'categoria'

""" VISTAS DE SERVICIO """

class ServicioListView(LoginRequiredMixin, EmprendimientoMixin, ListView):
    model = Servicio
    template_name = 'actividadeconomica/servicio_list.html'
    context_object_name = 'servicios'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('categoria')
        
        # Filtros adicionales
        search_query = self.request.GET.get('search', '')
        categoria_id = self.request.GET.get('categoria', '')
        
        if search_query:
            queryset = queryset.filter(descripcion__icontains=search_query)
        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        return queryset.order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class ServicioCreateView(LoginRequiredMixin, EmprendimientoMixin, CreateView):
    model = Servicio
    template_name = 'actividadeconomica/servicio_form.html'
    fields = ['descripcion', 'categoria', 'horas']
    success_url = reverse_lazy('servicio_list')
    success_message = 'Servicio creado exitosamente.'

class ServicioUpdateView(LoginRequiredMixin, EmprendimientoMixin, UpdateView):
    model = Servicio
    template_name = 'actividadeconomica/servicio_form.html'
    fields = ['descripcion', 'categoria', 'horas']
    success_url = reverse_lazy('servicio_list')
    success_message = 'Servicio actualizado exitosamente.'

class ServicioDeleteView(LoginRequiredMixin, EmprendimientoMixin, DeleteView):
    model = Servicio
    template_name = 'actividadeconomica/servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Servicio eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class ServicioDetailView(LoginRequiredMixin, EmprendimientoMixin, DetailView):
    model = Servicio
    template_name = 'actividadeconomica/servicio_detail.html'
    context_object_name = 'servicio'

""" VISTAS DE PRODUCTO """

class ProductoListView(LoginRequiredMixin, EmprendimientoMixin, ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('categoria')
        
        # Filtros adicionales
        search_query = self.request.GET.get('search', '')
        categoria_id = self.request.GET.get('categoria', '')
        
        if search_query:
            queryset = queryset.filter(descripcion__icontains=search_query)
        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        
        # Filtrar productos con stock bajo
        stock_bajo = self.request.GET.get('stock_bajo', '')
        if stock_bajo:
            queryset = queryset.filter(cantidad__lte=5)
        
        return queryset.order_by('-fecha_creacion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class ProductoCreateView(LoginRequiredMixin, EmprendimientoMixin, CreateView):
    model = Producto
    template_name = 'actividadeconomica/producto_form.html'
    fields = ['descripcion', 'categoria', 'cantidad']
    success_url = reverse_lazy('producto_list')
    success_message = 'Producto creado exitosamente.'

class ProductoUpdateView(LoginRequiredMixin, EmprendimientoMixin, UpdateView):
    model = Producto
    template_name = 'actividadeconomica/producto_form.html'
    fields = ['descripcion', 'categoria', 'cantidad']
    success_url = reverse_lazy('producto_list')
    success_message = 'Producto actualizado exitosamente.'

class ProductoDeleteView(LoginRequiredMixin, EmprendimientoMixin, DeleteView):
    model = Producto
    template_name = 'actividadeconomica/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Producto eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class ProductoDetailView(LoginRequiredMixin, EmprendimientoMixin, DetailView):
    model = Producto
    template_name = 'actividadeconomica/producto_detail.html'
    context_object_name = 'producto'