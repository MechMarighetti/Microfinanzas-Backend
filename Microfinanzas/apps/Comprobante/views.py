from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from .models import Comprobante, MedioPagoEnum, TipoComprobanteEnum
from django.contrib.auth.mixins import LoginRequiredMixin
from ..mixins import PreviousPageMixin


"""Vista convertida de funcion a clase"""
class IndexView(LoginRequiredMixin, PreviousPageMixin, ListView): 
    model = Comprobante
    template_name = 'index.html'
    context_object_name = 'comprobantes'
    
    def get_queryset(self):
        """Obtener todos los comprobantes"""
        return Comprobante.objects.all()
    
    def get_context_data(self, **kwargs):
        """Agregar datos adicionales al contexto"""
        context = super().get_context_data(**kwargs)
        context['ultimocomprobante'] = Comprobante.objects.last()
        return context
    

class CrearComprobanteView(LoginRequiredMixin, PreviousPageMixin, TemplateView):
    template_name = 'crear_comprobante.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'TipoComprobanteEnum': TipoComprobanteEnum,
            'MedioPagoEnum': MedioPagoEnum
        })
        return context
    
    '''def get(self, request):
        context = {
            'TipoComprobanteEnum': TipoComprobanteEnum,
            'MedioPagoEnum': MedioPagoEnum
        }
        return render(request, 'crear_comprobante.html', context)
    '''
    
    def post(self, request):
        try:
            # Obtener datos del formulario
            numero = request.POST.get('numero', '').strip()
            fecha = request.POST.get('fecha', '').strip()
            monto = request.POST.get('monto', '').strip()
            tipo = request.POST.get('tipo', '').strip()
            medio_pago = request.POST.get('medio_pago', '').strip()
            
            # Validaciones básicas
            if not all([numero, fecha, monto, tipo, medio_pago]):
                messages.error(request, 'Todos los campos son obligatorios.')
                return self._render_form_with_context()
            
            # Convertir monto a decimal
            try:
                monto_decimal = float(monto)
            except ValueError:
                messages.error(request, 'El monto debe ser un número válido.')
                return self._render_form_with_context()
            
            # Crear el comprobante
            comprobante = Comprobante.objects.create(
                numero=numero,
                fecha=fecha,
                monto=monto_decimal,
                tipo=tipo,
                medio_pago=medio_pago
            )
            
            messages.success(request, f'Comprobante {comprobante.numero} creado exitosamente!')
            return redirect('transaccion_create')
            
        except IntegrityError:
            messages.error(request, 'Ya existe un comprobante con ese número.')
            return self._render_form_with_context()
        except Exception as e:
            messages.error(request, f'Error al crear el comprobante: {str(e)}')
            return self._render_form_with_context()
    
    '''
    def _render_form_with_context(self):
        """Método helper para renderizar el formulario con el contexto"""
        context = {
            'TipoComprobanteEnum': TipoComprobanteEnum,
            'MedioPagoEnum': MedioPagoEnum
        }
        return render(self.request, 'crear_comprobante.html', context)
    '''

class DetalleComprobanteView(LoginRequiredMixin, PreviousPageMixin, DetailView):
    model = Comprobante
    template_name = 'detalle_comprobante.html'
    context_object_name = 'comprobante'
    pk_url_kwarg = 'comprobante_id' 
    
    def get_object(self, queryset=None):
        """Obtener el comprobante o mostrar error 404"""
        try:
            return get_object_or_404(Comprobante, id=self.kwargs.get('comprobante_id'))
        except Exception as e:
            messages.error(self.request, f'Error al obtener el comprobante: {str(e)}')
            # Redirigir al index en caso de error
            from django.shortcuts import redirect
            return redirect('index')
        