from django.conf.urls import url
from django.urls import path, include
from .views import (
	PlanMensualListarAPIView, 
	PlanMensualCrearAPIView, 
	PlanMensualEditarAPIView, 
	GastoGeneralListApiView, 
	GastoGeneralCreateApiView,
	GastoEditarAPIView)


urlpatterns = [
    url(r'^$', PlanMensualListarAPIView.as_view(), name='listar'),
    url(r'^add/$', PlanMensualCrearAPIView.as_view(), name='add'),
    url(r'^edit/(?P<user>\d+)', PlanMensualEditarAPIView.as_view(), name='edit_plan'),
    url(r'^gasto/list/$', GastoGeneralListApiView.as_view(), name='gasto_list'),
    url(r'^gasto/add/$', GastoGeneralCreateApiView.as_view(), name='gasto_add'),
    url(r'^gasto/edit/(?P<id>\d+)', GastoEditarAPIView.as_view(), name='edit_gasto'),
    #url(r'^carrito/list', CarritoListarAPIView.as_view(), name='listar'),
    #url(r'^carrito/by/(?P<user>\d+)', CarritoListByUserAPIView.as_view(), name='listarbyuser'),
    #url(r'^micarrito/by/(?P<user>\d+)', MiCarritoListByUserAPIView.as_view(), name='listarbyuser'),


]