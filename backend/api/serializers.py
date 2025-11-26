from rest_framework import serializers
from .models import Categoria, Producto, CaracteristicaProducto, Servicio, Contacto


class CategoriaSerializer(serializers.ModelSerializer):
    
    nombre_display = serializers.CharField(source='get_nombre_display', read_only=True)
    
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'nombre_display', 'descripcion', 'icon']


class CaracteristicaProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CaracteristicaProducto
        fields = ['id', 'descripcion', 'orden']


class ProductoSerializer(serializers.ModelSerializer):
    
    features = CaracteristicaProductoSerializer(many=True, read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    categoria_display = serializers.CharField(source='categoria.get_nombre_display', read_only=True)
    
    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'categoria', 'categoria_nombre', 'categoria_display',
            'icon', 'descripcion', 'precio', 'precio_numerico', 'features',
            'fabricante', 'modelo', 'destacado', 'stock', 'activo',
            'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']


class ProductoCreateSerializer(serializers.ModelSerializer):
    
    features = serializers.ListField(
        child=serializers.CharField(max_length=255),
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'categoria', 'icon', 'descripcion', 
            'precio', 'precio_numerico', 'fabricante', 'modelo',
            'destacado', 'stock', 'activo', 'features'
        ]
    
    def create(self, validated_data):
        features_data = validated_data.pop('features', [])
        producto = Producto.objects.create(**validated_data)
        
        for idx, feature in enumerate(features_data):
            CaracteristicaProducto.objects.create(
                producto=producto,
                descripcion=feature,
                orden=idx
            )
        
        return producto


class ServicioSerializer(serializers.ModelSerializer):
    
    nivel_complejidad_display = serializers.CharField(
        source='get_nivel_complejidad_display', 
        read_only=True
    )
    
    class Meta:
        model = Servicio
        fields = [
            'id', 'nombre', 'icon', 'descripcion', 'precio', 'precio_numerico',
            'duracion_estimada', 'nivel_complejidad', 'nivel_complejidad_display',
            'destacado', 'activo', 'fecha_creacion', 'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']


class ContactoSerializer(serializers.ModelSerializer):
    
    producto_nombre = serializers.CharField(
        source='producto_interes.nombre', 
        read_only=True
    )
    servicio_nombre = serializers.CharField(
        source='servicio_interes.nombre', 
        read_only=True
    )
    
    class Meta:
        model = Contacto
        fields = [
            'id', 'nombre', 'email', 'telefono', 'mensaje',
            'producto_interes', 'producto_nombre',
            'servicio_interes', 'servicio_nombre',
            'fecha_envio', 'leido', 'respondido'
        ]
        read_only_fields = ['fecha_envio', 'leido', 'respondido']


class ContactoCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje', 'producto_interes', 'servicio_interes']
