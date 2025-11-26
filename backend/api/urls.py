"""
URLs de la API
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ServicioViewSet, ContactoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'servicios', ServicioViewSet, basename='servicio')
router.register(r'contactos', ContactoViewSet, basename='contacto')

urlpatterns = [
    path('', include(router.urls)),
]
