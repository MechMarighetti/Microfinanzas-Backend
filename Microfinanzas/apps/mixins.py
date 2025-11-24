#from django.urls import reverse

class PreviousPageMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        referer = self.request.META.get('HTTP_REFERER')
        
        # Solo usa el referer si existe y no es la página actual
        if referer and referer != self.request.build_absolute_uri():
            context['previous_page'] = referer
        else:
            context['previous_page'] = None
            
        return context
        

    '''def get_previous_page(self, default_view_name=None):
        """
        Obtiene la URL anterior de forma segura
        """
        # 1. Intentar con el parámetro 'next' en la URL
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        
        # 2. Intentar con HTTP_REFERER
        referer = self.request.META.get('HTTP_REFERER')
        if referer and self.is_safe_url(referer):
            return referer
        
        # 3. Usar URL por defecto
        if default_view_name:
            return reverse(default_view_name)
        return reverse('transaccion_list')  # Ajusta según tu URL por defecto
    
    
    def get_context_data(self, **kwargs):
        """Agrega la URL de retorno al contexto"""
        context = super().get_context_data(**kwargs)
        context['return_url'] = self.get_previous_page()
        return context
        '''