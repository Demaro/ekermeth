from django.conf.urls import url
from django.urls import path, include
from .views import ProductoListarAPIView, ProductoCrearAPIView, CategoriaListarAPIView, CarritoListarAPIView, CarritoListByUserAPIView, MiCarritoListByUserAPIView

urlpatterns = [
    url(r'^$', ProductoListarAPIView.as_view(), name='listar'),
    url(r'^add/$', ProductoCrearAPIView.as_view(), name='add'),
    url(r'^categorias/', CategoriaListarAPIView.as_view(), name='list_category'),
    url(r'^carrito/list', CarritoListarAPIView.as_view(), name='listar'),
    url(r'^carrito/by/(?P<user>\d+)', CarritoListByUserAPIView.as_view(), name='listarbyuser'),
    url(r'^micarrito/by/(?P<user>\d+)', MiCarritoListByUserAPIView.as_view(), name='listarbyuser'),


]