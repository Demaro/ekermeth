from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,


)


from .serializers import ProductSerializer, ProductCrearSerializer, CategorySerializer, CarritoCompraSerializer, MiCarritoCompraSerializer
from products.models import Producto, Categoria
#
#PERMISOS
#
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

class ProductoListarAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class CategoriaListarAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = Categoria.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class ProductoCrearAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = ProductCrearSerializer
    queryset = Producto.objects.all()
    permission_classes = [AllowAny]



