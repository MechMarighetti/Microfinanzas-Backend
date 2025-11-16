from django.db import models

class UnidadMedidaEnum(models.TextChoices):
    UNIDAD = "UNI", "Unidad"
    KILOGRAMO = "KG", "Kilogramo"
    LITRO = "LT", "Litro"
    METRO = "M", "Metro"
    METRO_CUADRADO = "M2", "Metro cuadrado"
    METRO_CUBICO = "M3", "Metro cúbico"
    HORA = "HR", "Hora"
    JUEGO = "JG", "Juego"
    PAQUETE = "PAQ", "Paquete"
    DOCENA = "DOC", "Docena"
    KILOWATT = "KW", "Kilowatt"
    TONELADA = "TN", "Tonelada"
    PAR = "PAR", "Par"
    CAJA = "CJ", "Caja"
    BOBINA = "BOB", "Bobina"



class DetalleIngreso(models.Model):
    fecha = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    unidad_medida = models.CharField(
        max_length=4,
        choices=UnidadMedidaEnum.choices
    )

    
    
    actividadEconomica = models.ForeignKey('Ingreso', on_delete=models.CASCADE, null=True, blank=True)
    transaccion = models.ForeignKey('Transaccion', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Detalle Ingreso {self.unique_id} - {self.fecha}"



