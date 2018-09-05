from django.conf.urls import url
from django.urls import path, include
from .views import PlanMensualListarAPIView, PlanMensualCrearAPIView, PlanMensualEditarAPIView

urlpatterns = [
    url(r'^$', PlanMensualListarAPIView.as_view(), name='listar'),
    url(r'^add/$', PlanMensualCrearAPIView.as_view(), name='add'),
    url(r'^edit/(?P<id>\d+)', PlanMensualEditarAPIView.as_view(), name='edit_plan'),
    #url(r'^carrito/list', CarritoListarAPIView.as_view(), name='listar'),
    #url(r'^carrito/by/(?P<user>\d+)', CarritoListByUserAPIView.as_view(), name='listarbyuser'),
    #url(r'^micarrito/by/(?P<user>\d+)', MiCarritoListByUserAPIView.as_view(), name='listarbyuser'),


]