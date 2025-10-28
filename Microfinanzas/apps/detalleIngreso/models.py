from django.db import models

class UnidadMedida(models.Model):
    unique_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class DetalleIngreso(models.Model):
    unique_id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    
    
    ingreso = models.ForeignKey('Ingreso', on_delete=models.CASCADE, null=True, blank=True)
    servicio = models.ForeignKey('Servicio', on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Detalle Ingreso {self.unique_id} - {self.fecha}"


# Create your models here.
