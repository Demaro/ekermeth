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


from .serializers import PlanMensualSerializer, PlanMensualCrearActualizarSerializer
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
    permission_classes = [AllowAny]


class PlanMensualCrearAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = PlanMensualCrearActualizarSerializer
    queryset = Plan_mensual.objects.all()
    permission_classes = [AllowAny]


class PlanMensualEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    
    serializer_class = PlanMensualCrearActualizarSerializer
    queryset = Plan_mensual.objects.all()
    lookup_field = 'id'
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)





