from django.db import models

class TipoComprobanteEnum(models.TextChoices):
    FACTURA_A = 'FA', 'Factura A'
    FACTURA_B = 'FB', 'Factura B'
    FACTURA_C = 'FC', 'Factura C'
    NOTA_CREDITO = 'NC', 'Nota de Crédito'
    NOTA_DEBITO = 'ND', 'Nota de Débito'
    RECIBO = 'RC', 'Recibo'
    REMITO = 'RM', 'Remito'
    OTRO = 'OT', 'Otro'

class MedioPagoEnum(models.TextChoices):
    EFECTIVO = 'EF', 'Efectivo'
    TARJETA_CREDITO = 'TC', 'Tarjeta de Crédito'
    TARJETA_DEBITO = 'TD', 'Tarjeta de Débito'
    TRANSFERENCIA = 'TR', 'Transferencia'
    QR = 'QR', 'Pago QR'
    MODO = 'MD', 'Pago MODO'
    MERCADO_PAGO = 'MP', 'Mercado Pago'
    CHEQUE = 'CH', 'Cheque'
    OTRO = 'OT', 'Otro'

class Comprobante(models.Model):
    #proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(
        max_length=2,
        choices=TipoComprobanteEnum.choices,
        default=TipoComprobanteEnum.FACTURA_B
    )
    medio_pago = models.CharField(
        max_length=2,
        choices=MedioPagoEnum.choices,
        default=MedioPagoEnum.EFECTIVO
    )

    def __str__(self):
        return f"Comprobante {self.tipo} - {self.numero} - {self.monto}"



