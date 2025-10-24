from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from .models import Comprobante, MedioPagoEnum, TipoComprobanteEnum
from django.contrib.auth.mixins import LoginRequiredMixin


"""Vista convertida de funcion a clase"""
class IndexView(ListView): 
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
    
""" def index(request):
    comprobantes = Comprobante.objects.all()
    ultimocomprobante = Comprobante.objects.last()
    return render(request, 'index.html', {'comprobantes': comprobantes})
 """
class CrearComprobanteView(View):
    """Vista para crear nuevos comprobantes"""
    
    def get(self, request):
        
        """Muestra el formulario vacío"""
        context = {
            'TipoComprobanteEnum': TipoComprobanteEnum,
            'MedioPagoEnum': MedioPagoEnum
        }
        return render(request, 'crear_comprobante.html', context)
    
    def post(self, request):
        """Procesa el formulario de creación"""
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
            return redirect('index')
            
        except IntegrityError:
            messages.error(request, 'Ya existe un comprobante con ese número.')
            return self._render_form_with_context()
        except Exception as e:
            messages.error(request, f'Error al crear el comprobante: {str(e)}')
            return self._render_form_with_context()
    
    def _render_form_with_context(self):
        """Método helper para renderizar el formulario con el contexto"""
        context = {
            'TipoComprobanteEnum': TipoComprobanteEnum,
            'MedioPagoEnum': MedioPagoEnum
        }
        return render(self.request, 'crear_comprobante.html', context)
    
""" def crear_comprobante(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            numero = request.POST['numero']
            fecha = request.POST['fecha']
            monto = request.POST['monto']
            tipo = request.POST['tipo']
            medio_pago = request.POST['medio_pago']
            
            # Validaciones básicas
            if not all([numero, fecha, monto, tipo, medio_pago]):
                messages.error(request, 'Todos los campos son obligatorios.')
                return render(request, 'crear_comprobante.html', {
                'TipoComprobanteEnum': TipoComprobanteEnum,
                'MedioPagoEnum': MedioPagoEnum
            })
            
            # Crear el comprobante usando objects.create
            comprobante = Comprobante.objects.create(
                numero=numero,
                fecha=fecha,
                monto=monto,
                tipo=tipo,
                medio_pago=medio_pago
            )
            
            messages.success(request, f'Comprobante {comprobante.numero} creado exitosamente!')
            return redirect('index')
            
        except Exception as e:
            messages.error(request, f'Error al crear el comprobante: {str(e)}')
            return render(request, 'crear_comprobante.html', {
                'TipoComprobanteEnum': TipoComprobanteEnum,
                'MedioPagoEnum': MedioPagoEnum
            })
    
    # Método GET - mostrar formulario vacío
    return render(request, 'crear_comprobante.html', {
        'TipoComprobanteEnum': TipoComprobanteEnum,
        'MedioPagoEnum': MedioPagoEnum
    })
 """

class DetalleComprobanteView(DetailView):
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
        
""" def detalle_comprobante(request, comprobante_id):
    try:
        comprobante = Comprobante.objects.get(id=comprobante_id)
        return render(request, 'detalle_comprobante.html', {'comprobante': comprobante})
    except Comprobante.DoesNotExist:
        messages.error(request, 'El comprobante no existe.')
        return redirect('index')
    except Exception as e:
        messages.error(request, f'Error al obtener el comprobante: {str(e)}')
        return redirect('index') """