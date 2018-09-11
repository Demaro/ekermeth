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


from .serializers import PlanMensualSerializer, PlanMensualCrearActualizarSerializer, GastoGeneralCreateSerializer
from plan_mensual.models import Plan_mensual, Gasto_general
#
#PERMISOS

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

class PlanMensualListarAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = Plan_mensual.objects.all()
    serializer_class = PlanMensualSerializer
    permission_classes = [IsAuthenticated]



class PlanMensualCrearAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = PlanMensualCrearActualizarSerializer
    queryset = Plan_mensual.objects.all()
    permission_classes = [IsAuthenticated]


class PlanMensualEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    
    serializer_class = PlanMensualCrearActualizarSerializer
    queryset = Plan_mensual.objects.all()
    lookup_field = 'user'
    permission_classes = [AllowAny]


class GastoGeneralListApiView(ListAPIView):
    """
    Serializador para listar todos los gastos
    """
    serializer_class = GastoGeneralCreateSerializer
    queryset = Gasto_general.objects.all()
    permission_classes = [AllowAny]

class GastoGeneralCreateApiView(CreateAPIView):
    """
    Serializador Agregar nuevo Gasto
    """
    serializer_class = GastoGeneralCreateSerializer
    queryset = Gasto_general.objects.all()
    permission_classes = [AllowAny]

class GastoEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un GASTO por ID
    """
    
    serializer_class = GastoGeneralCreateSerializer
    queryset = Gasto_general.objects.all()
    lookup_field = 'id'
    permission_classes = [AllowAny]





