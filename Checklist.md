## Checklist para terminar este TP

Generá consejos prácticos y sus implementaciones en pocas líneas para sistematizar lo que hermos aprendido y usado. Priorizá sintaxis y procedimiento. No generes código mas alla de ciertos snippets. Dejo dos ejemplos en templates. Hacer consejos mirando el repositorio. El foco en tratar de reutilizar. 
Este documento será la documentacion de la app y una guia de lo que aprendimos en backend este cuatrimestre.

---

### Templates

**Herencia de plantillas:**
```
{% extends 'base.html' %}
{% block content %}
    <h1>Mi contenido</h1>
{% endblock %}
```

**Incluir componentes reutilizables:**
```
{% include 'nav.html' %}
{% include 'footer.html' %}
```

**Paso de contexto a templates:**
```python
# En views.py
context = {'items': items, 'titulo': 'Listado'}
return render(request, 'template.html', context)

# En template.html
<h1>{{ titulo }}</h1>
{% for item in items %}
    <p>{{ item.nombre }}</p>
{% endfor %}
```

**Filtros de plantilla:**
```
{{ nombre|upper }}  # Convierte a mayúsculas
{{ precio|floatformat:2 }}  # Formatea decimales
{% if usuario.is_authenticated %} ... {% endif %}
```

---

### Static

**Configuración en settings.py:**
```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'  # Producción
```

**Cargar archivos estáticos en templates:**
```
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
<img src="{% static 'images/logo.png' %}">
```

**Estructura recomendada:**
```
static/
  ├── css/
  ├── js/
  ├── images/
  └── vendor/
```

---

### Vistas basadas en clases (Class-Based Views)

**ListView - Mostrar lista de objetos:**
```python
class ComprobanteListView(LoginRequiredMixin, ListView):
    model = Comprobante
    template_name = 'comprobante_list.html'
    context_object_name = 'comprobantes'
    paginate_by = 10
    
    def get_queryset(self):
        return Comprobante.objects.filter(usuario=self.request.user).order_by('-fecha')
```

**CreateView - Formulario de creación:**
```python
class ComprobanteCreateView(LoginRequiredMixin, CreateView):
    model = Comprobante
    template_name = 'comprobante_form.html'
    fields = ['numero', 'fecha', 'monto', 'tipo']
    success_url = reverse_lazy('comprobante_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Creado exitosamente.')
        return super().form_valid(form)
```

**DetailView - Detalle de un objeto:**
```python
class ComprobanteDetailView(LoginRequiredMixin, DetailView):
    model = Comprobante
    template_name = 'comprobante_detail.html'
    pk_url_kwarg = 'comprobante_id'  # Del URL
```

**Mixins útiles:**
- `LoginRequiredMixin`: Requiere usuario autenticado
- `UserPassesTestMixin`: Validaciones personalizadas
- `PermissionRequiredMixin`: Verificar permisos específicos

---

### Configuración de URLs

**En urls.py principal (Microfinanzas/urls.py):**
```python
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comprobante/', include('apps.comprobante.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('', include('apps.emprendimiento.urls')),
]
```

**En urls.py de cada app (apps/usuario/urls.py):**
```python
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
```

**Nombres descriptivos y reutilizables:**
```python
# URL en template
<a href="{% url 'comprobante_detail' pk=obj.id %}">Ver detalle</a>

# URL en Python
from django.urls import reverse_lazy
success_url = reverse_lazy('comprobante_list')
```

---

### Formularios en Django

**Formulario basado en modelo (ModelForm):**
```python
from django import forms
from .models import Comprobante

class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = ['numero', 'fecha', 'monto', 'tipo', 'medio_pago']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'monto': forms.NumberInput(attrs={'step': '0.01'}),
        }
```

**Formulario personalizado (UserCreationForm):**
```python
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo", required=True)
    dni = forms.CharField(label="DNI", max_length=20)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'dni', 'password1', 'password2']
```

**Validar y guardar:**
```python
if form.is_valid():
    objeto = form.save(commit=False)
    objeto.usuario = request.user
    objeto.save()
else:
    messages.error(request, 'Errores en el formulario')
```

---

### Admin Built-in de Django

**Registro de modelo:**
```python
from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'dni', 'email', 'rol', 'miembroActivo')
    search_fields = ('username', 'dni', 'email')
    list_filter = ('is_active', 'is_staff', 'rol')
    readonly_fields = ('fechaDeCreacion',)
```

**Opciones útiles:**
```python
list_display = (...)  # Columnas a mostrar
list_filter = (...)  # Filtros laterales
search_fields = (...)  # Campos buscables
ordering = (...)  # Orden por defecto
readonly_fields = (...)  # Solo lectura
fieldsets = (...)  # Agrupar campos
```

**Acceso desde navegador:**
```
http://localhost:8000/admin/
Username: admin
```

---

### Settings

**Configuración esencial en settings.py:**
```python
# BASE DE DATOS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# USUARIO PERSONALIZADO
AUTH_USER_MODEL = 'usuario.Usuario'

# APPS INSTALADAS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'apps.comprobante',
    'apps.usuario',
    'apps.transaccion',
]

# TEMPLATES
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates/'],
    'APP_DIRS': True,
}]

# RUTAS DE LOGIN
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
```

**Variables de desarrollo vs producción:**
```python
DEBUG = True  # Solo en desarrollo
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Agregar dominios
SECRET_KEY = 'change-me-in-production'
```

---

### Uso de Shell para pruebas

**Acceder a Django Shell:**
```
python manage.py shell
```

**Importar y consultar modelos:**
```python
from apps.comprobante.models import Comprobante
from apps.usuario.models import Usuario

# Crear
usuario = Usuario.objects.create(username='test', email='test@mail.com')
comprobante = Comprobante.objects.create(numero='001', monto=100.00)

# Leer
comprobantes = Comprobante.objects.all()
primer_comprobante = Comprobante.objects.first()

# Actualizar
comprobante.monto = 150.00
comprobante.save()

# Eliminar
comprobante.delete()
```

**Consultas útiles:**
```python
Comprobante.objects.filter(monto__gt=100)  # Mayor que
Comprobante.objects.filter(fecha__year=2025)  # Por año
Comprobante.objects.count()  # Contar
Comprobante.objects.values_list('numero', flat=True)  # Solo un campo
```

---

### Queries (Consultas ORM)

**Operadores de filtro:**
```python
# Igualdad
Comprobante.objects.filter(tipo='FA')

# Comparación
Comprobante.objects.filter(monto__gt=100)  # Mayor que
Comprobante.objects.filter(monto__lte=1000)  # Menor o igual

# Búsqueda de texto
Comprobante.objects.filter(numero__icontains='001')  # Case-insensitive

# Fechas
Comprobante.objects.filter(fecha__year=2025)
Comprobante.objects.filter(fecha__gte='2025-01-01')

# Q objects (OR)
from django.db.models import Q
Comprobante.objects.filter(Q(tipo='FA') | Q(tipo='FB'))
```

**Optimizaciones:**
```python
# Select_related (ForeignKey)
Comprobante.objects.select_related('usuario')

# Prefetch_related (ManyToMany, Reverse FK)
Emprendimiento.objects.prefetch_related('servicios')

# only() y defer()
Usuario.objects.only('username', 'email')
Usuario.objects.defer('direccion')
```

**Agregaciones:**
```python
from django.db.models import Sum, Count, Avg

Comprobante.objects.aggregate(total=Sum('monto'))
Comprobante.objects.values('tipo').annotate(count=Count('id'))
```

---

### Modelos

**Definir un modelo:**
```python
class Comprobante(models.Model):
    # Campos
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(
        max_length=2,
        choices=TipoComprobanteEnum.choices,
        default=TipoComprobanteEnum.FACTURA_B
    )
    
    # Métodos
    def __str__(self):
        return f"Comprobante {self.numero}"
    
    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"
        ordering = ['-fecha']
```

**Relaciones:**
```python
# ForeignKey (Uno a muchos)
class Servicio(models.Model):
    emprendimiento = models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    
# ManyToMany
class Producto(models.Model):
    categorias = models.ManyToManyField(Categoria)

# OneToOneField
class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
```

**Enumeraciones como TextChoices:**
```python
class TipoComprobanteEnum(models.TextChoices):
    FACTURA_A = 'FA', 'Factura A'
    FACTURA_B = 'FB', 'Factura B'
    NOTA_CREDITO = 'NC', 'Nota de Crédito'
```

**Migraciones:**
```bash
python manage.py makemigrations  # Crear cambios
python manage.py migrate  # Aplicar cambios
python manage.py showmigrations  # Ver migraciones
```

---

### Auth Custom User en Django

**Crear usuario personalizado:**
```python
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
    miembroActivo = models.BooleanField(default=True)
    fechaDeCreacion = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
```

**Configurar en settings.py:**
```python
AUTH_USER_MODEL = 'usuario.Usuario'  # Punto de referencia: 'app.Modelo'
```

**Vistas de autenticación:**
```python
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class RegisterView(CreateView):
    model = Usuario
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
```

**Verificar autenticación en vistas:**
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class ProtectedView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'next'
```

**En templates:**
```html
{% if user.is_authenticated %}
    Bienvenido, {{ user.username }}
    <a href="{% url 'logout' %}">Salir</a>
{% else %}
    <a href="{% url 'login' %}">Ingresar</a>
{% endif %}
```

---

## Comandos útiles

```bash
# Crear proyecto
django-admin startproject nombre_proyecto

# Crear app
python manage.py startapp nombre_app

# Servidor de desarrollo
python manage.py runserver

# Crear usuario admin
python manage.py createsuperuser

# Entrar al shell
python manage.py shell

# Ver estado de migraciones
python manage.py showmigrations

# Resetear base de datos
python manage.py flush
```

---

## Recursos recomendados

- **Django Docs:** https://docs.djangoproject.com/
- **Django ORM:** https://docs.djangoproject.com/en/stable/topics/db/models/
- **Class-Based Views:** https://docs.djangoproject.com/en/stable/topics/class-based-views/
- **Templates:** https://docs.djangoproject.com/en/stable/topics/templates/

---

**Última actualización:** Noviembre 2025  
**Proyecto:** Microfinanzas - Backend Django  
**Estado:** Documentado

