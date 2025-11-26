from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    
    CATEGORIAS_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('cloud', 'Cloud'),
        ('seguridad', 'Seguridad'),
    ]
    
    nombre = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES, unique=True)
    descripcion = models.TextField(blank=True)
    icon = models.CharField(max_length=10, default='📦')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
    
    def __str__(self):
        return self.get_nombre_display()


class Producto(models.Model):
    
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos'
    )
    icon = models.CharField(max_length=10, default='💻')
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    precio_numerico = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        help_text="Precio en formato numérico para ordenamiento"
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fabricante = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    destacado = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['categoria', 'activo']),
            models.Index(fields=['destacado']),
        ]
    
    def __str__(self):
        return self.nombre


class CaracteristicaProducto(models.Model):
    
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        related_name='features'
    )
    descripcion = models.CharField(max_length=255)
    orden = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Característica de Producto'
        verbose_name_plural = 'Características de Productos'
        ordering = ['orden', 'id']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.descripcion[:50]}"


class Servicio(models.Model):
    
    nombre = models.CharField(max_length=200)
    icon = models.CharField(max_length=10, default='🛠️')
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    precio_numerico = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        help_text="Precio en formato numérico para ordenamiento"
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    duracion_estimada = models.CharField(
        max_length=100, 
        blank=True,
        help_text="Ej: 2-4 semanas"
    )
    nivel_complejidad = models.CharField(
        max_length=20,
        choices=[
            ('basico', 'Básico'),
            ('intermedio', 'Intermedio'),
            ('avanzado', 'Avanzado'),
            ('empresarial', 'Empresarial'),
        ],
        default='intermedio'
    )
    destacado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-fecha_creacion']
        indexes = [
            models.Index(fields=['activo', 'destacado']),
        ]
    
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    respondido = models.BooleanField(default=False)
    producto_interes = models.ForeignKey(
        Producto, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='contactos'
    )
    servicio_interes = models.ForeignKey(
        Servicio, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='contactos'
    )
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.nombre} - {self.email} ({self.fecha_envio.strftime('%d/%m/%Y')})"
