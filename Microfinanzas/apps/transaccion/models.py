from django.db import models
from ..Comprobante.models import Comprobante
from ..emprendimiento.models import Emprendimiento

class Ingreso(models.Model):
    fecha = models.DateField(default=date.today)
    importe = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.CharField(max_length=100)

    comprobante_id = models.ForeignKey(Comprobante, on_delete=models.CASCADE, related_name='ingresos')
    emprendimiento_id = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE, related_name='ingresos')

    def __str__(self):
        return f"Fecha: {self.fecha}\nImporte: {self.importe}\nDescripción: {self.descripcion}"

class Egreso(models.Model):
    fecha = models.DateField(default=date.today)
    importe = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.CharField(max_length=100)

    comprobante_id = models.ForeignKey(Comprobante, on_delete=models.CASCADE, related_name='egresos')
    emprendimiento_id = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE, related_name='egresos')

    def __str__(self):
        return f"Fecha: {self.fecha}\nImporte: {self.importe}\nDescripción: {self.descripcion}"