"""
Configuración del panel de administración de Django
"""
from django.contrib import admin
from .models import Categoria, Producto, CaracteristicaProducto, Servicio, Contacto


class CaracteristicaProductoInline(admin.TabularInline):
    model = CaracteristicaProducto
    extra = 3


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'icon', 'descripcion']
    search_fields = ['nombre', 'descripcion']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'fabricante', 'destacado', 'stock', 'activo', 'fecha_creacion']
    list_filter = ['categoria', 'destacado', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion', 'fabricante', 'modelo']
    list_editable = ['destacado', 'activo']
    inlines = [CaracteristicaProductoInline]
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'categoria', 'icon', 'descripcion')
        }),
        ('Precio', {
            'fields': ('precio', 'precio_numerico')
        }),
        ('Detalles', {
            'fields': ('fabricante', 'modelo', 'stock')
        }),
        ('Estado', {
            'fields': ('destacado', 'activo')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'nivel_complejidad', 'destacado', 'activo', 'fecha_creacion']
    list_filter = ['nivel_complejidad', 'destacado', 'activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['destacado', 'activo']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'icon', 'descripcion')
        }),
        ('Precio y Duración', {
            'fields': ('precio', 'precio_numerico', 'duracion_estimada')
        }),
        ('Clasificación', {
            'fields': ('nivel_complejidad', 'destacado', 'activo')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'fecha_envio', 'leido', 'respondido']
    list_filter = ['leido', 'respondido', 'fecha_envio']
    search_fields = ['nombre', 'email', 'mensaje']
    list_editable = ['leido', 'respondido']
    readonly_fields = ['fecha_envio']
    
    fieldsets = (
        ('Información de Contacto', {
            'fields': ('nombre', 'email', 'telefono')
        }),
        ('Mensaje', {
            'fields': ('mensaje',)
        }),
        ('Interés', {
            'fields': ('producto_interes', 'servicio_interes')
        }),
        ('Estado', {
            'fields': ('leido', 'respondido', 'fecha_envio')
        }),
    )
