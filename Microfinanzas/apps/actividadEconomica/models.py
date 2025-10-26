from django.db import models
from emprendimiento.models import Emprendimiento

class Categoria(models.Model):

    nombre= models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='servicios')
    horas = models.IntegerField(default=0)
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE, related_name='servicios')

    def __str__(self):
        return self.descripcion
    

class Producto(models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    cantidad = models.IntegerField(default=0)
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.descripcion, self.cantidad