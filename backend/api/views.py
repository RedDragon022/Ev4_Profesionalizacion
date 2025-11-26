from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categoria, Producto, Servicio, Contacto
from .serializers import (
    CategoriaSerializer, ProductoSerializer, ProductoCreateSerializer,
    ServicioSerializer, ContactoSerializer, ContactoCreateSerializer
)


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(activo=True).select_related('categoria').prefetch_related('features')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['categoria', 'destacado', 'activo']
    search_fields = ['nombre', 'descripcion', 'fabricante', 'modelo']
    ordering_fields = ['precio_numerico', 'fecha_creacion', 'nombre']
    ordering = ['-fecha_creacion']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ProductoCreateSerializer
        return ProductoSerializer
    
    @action(detail=False, methods=['get'])
    def destacados(self, request):
        productos = self.queryset.filter(destacado=True)
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        categoria = request.query_params.get('categoria', None)
        if categoria:
            productos = self.queryset.filter(categoria__nombre=categoria)
            serializer = self.get_serializer(productos, many=True)
            return Response(serializer.data)
        return Response({'error': 'Parámetro categoria requerido'}, status=400)


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.filter(activo=True)
    serializer_class = ServicioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['precio_numerico', 'fecha_creacion', 'nombre']
    ordering = ['-fecha_creacion']
    
    @action(detail=False, methods=['get'])
    def destacados(self, request):
        servicios = self.queryset.filter(destacado=True)
        serializer = self.get_serializer(servicios, many=True)
        return Response(serializer.data)


class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering = ['-fecha_envio']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ContactoCreateSerializer
        return ContactoSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response({
            'success': True,
            'message': 'Mensaje enviado correctamente. Nos pondremos en contacto pronto.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['patch'])
    def marcar_leido(self, request, pk=None):
        contacto = self.get_object()
        contacto.leido = True
        contacto.save()
        serializer = self.get_serializer(contacto)
        return Response(serializer.data)
