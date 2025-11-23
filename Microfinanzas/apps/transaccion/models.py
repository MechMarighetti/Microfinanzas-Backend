from datetime import date
from django.db import models

from ..comprobante.models import Comprobante
from ..emprendimiento.models import Emprendimiento
from ..detalleIngreso.models import DetalleIngreso

class TipoTrx(models.TextChoices):
    INGRESO = "IN", "Ingreso"
    EGRESO = "EG", "Egreso"

class Transaccion(models.Model):
    fecha = models.DateField(default=date.today)
    importe = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    


    tipoTrx = models.CharField(
        max_length=2,        
        choices=TipoTrx.choices,
        default=TipoTrx.INGRESO,
    )
    comprobante_id = models.ForeignKey(Comprobante, on_delete=models.CASCADE, related_name='trx')
    emprendimiento_id = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE, related_name='trx')
    detalle_id = models.ForeignKey(DetalleIngreso, on_delete=models.CASCADE, related_name='trx', null=True, blank=True)
