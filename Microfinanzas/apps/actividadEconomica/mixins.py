from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import Http404
from emprendimiento.models import Emprendimiento

class EmprendimientoMixin:
    """Mixin para manejar la relación con el emprendimiento del usuario"""
    
    def get_emprendimiento_user(self):
        """Obtiene el emprendimiento del usuario actual"""
        user = self.request.user
        
        # Primero intenta con emprendimiento propio (para owners)
        if hasattr(user, 'emprendimiento_propio') and user.emprendimiento_propio:
            return user.emprendimiento_propio
        
        # Luego con el emprendimiento al que pertenece
        if hasattr(user, 'emprendimiento') and user.emprendimiento:
            return user.emprendimiento
        
        # Si no tiene emprendimiento, muestra error
        raise Http404("No tienes un emprendimiento asignado.")
    
    def get_queryset(self):
        """Filtra los objetos por el emprendimiento del usuario"""
        queryset = super().get_queryset()
        emprendimiento = self.get_emprendimiento_user()
        return queryset.filter(emprendimiento=emprendimiento)
    
    def form_valid(self, form):
        """Asigna automáticamente el emprendimiento al objeto"""
        if hasattr(form.instance, 'emprendimiento'):
            form.instance.emprendimiento = self.get_emprendimiento_user()
        
        messages.success(self.request, self.success_message)
        return super().form_valid(form)