from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Comprobante, MedioPagoEnum, TipoComprobanteEnum

def index(request):
    comprobantes = Comprobante.objects.all()
    ultimocomprobante = Comprobante.objects.last()
    return render(request, 'index.html', {'comprobantes': comprobantes})


def crear_comprobante(request):
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

def detalle_comprobante(request, comprobante_id):
    try:
        comprobante = Comprobante.objects.get(id=comprobante_id)
        return render(request, 'detalle_comprobante.html', {'comprobante': comprobante})
    except Comprobante.DoesNotExist:
        messages.error(request, 'El comprobante no existe.')
        return redirect('index')
    except Exception as e:
        messages.error(request, f'Error al obtener el comprobante: {str(e)}')
        return redirect('index')