from django.db import models
from apps.usuario.models import Usuario

class Emprendimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprendimientos')

    def __str__(self):
        return self.nombre

# Create your models here.
