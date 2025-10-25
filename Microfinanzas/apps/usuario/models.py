from django.db import models
from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    ROLES = (
      ('owner', 'Dueño'),
      ('marketing', 'Marketing'),
      ('finanzas', 'Finanzas'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='owner')
    cuit = models.CharField(max_length=20, unique=True, null=True, blank=True)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    miembroActivo = models.BooleanField(default=True)
    fechaDeCreacion= models.DateField(null=True, blank=True)

   
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def str(self):
        return f"{self.username} ({self.get_role_display()})"


# Create your models here.
