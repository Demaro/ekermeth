from cuentas.models import User
from rest_framework import serializers
from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError,    
	EmailField,
	CharField,
	IntegerField,
	ValidationError,
	
)
from django.db.models import Q

from rest_framework.validators import UniqueValidator
from django.utils.translation import ugettext_lazy as _

from rest_framework.compat import authenticate
from plan_mensual.models import Plan_mensual, Gasto_general
from cuentas.api.serializers import UsuarioSerializer


class PlanMensualSerializer(ModelSerializer):
	user =	UsuarioSerializer(read_only=True)
	class Meta:
		model = Plan_mensual
		fields = ('id','user','sueldo', 'diario', 'gasto_general', 'date_start', 'total')

'''
class ProductSerializer(ModelSerializer):
	user = UsuarioSerializer(read_only=True)
	categoria = CategorySerializer(read_only=True)
	class Meta:
		model = Producto
		fields = ('id','name','description', 'user', 'categoria', 'precio','date', 'url_image')


class ProductSerializerforCarrito(ModelSerializer):
	categoria = CategorySerializer(read_only=True)
	class Meta:
		model = Producto
		fields = ('id', 'name', 'precio', 'categoria','url_image')

'''


class GastoGeneralCreateSerializer(ModelSerializer):

	class Meta:
		model = Gasto_general
		fields = [
		'id',
		'name',
		'value'
		]


class PlanMensualByUserSerializer(ModelSerializer):
	
	class Meta:
		model = Plan_mensual
		fields = [
			'id',
			'user',
			'sueldo',
			'diario',
			'gasto_general',
			'total'

		]


class PlanMensualByUserManySerializer(ModelSerializer):
	gasto_general = GastoGeneralCreateSerializer(many=True, read_only=True)
	class Meta:
		model = Plan_mensual
		fields = [
			'id',
			'user',
			'gasto_general',

		]


class PlanMensualCrearActualizarSerializer(ModelSerializer):
	
	class Meta:
		model = Plan_mensual
		fields = [
			'id',
			'user',
			'sueldo',
			'diario',
			'gasto_general',
			'total'

		]












