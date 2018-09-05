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

class PlanMensualCrearActualizarSerializer(ModelSerializer):
	#name = serializers.EmailField(validators=[UniqueValidator(queryset=Producto.objects.all(),
	#message="Ya existe un producto con este correo", )])
	#email2 = EmailField(label = 'Confirm Email')
	class Meta:
		model = Plan_mensual
		fields = [
			'user',
			'sueldo',
			'diario',
			'gasto_general',
			'date_start',
			'total'

		]

	def create(self, validated_data):
		user = validated_data['user']
		sueldo = validated_data['sueldo']
		diario = validated_data['diario']
		gasto_general = validated_data['gasto_general']
		date_start = validated_data['date_start']
		plan_obj = Producto(
			user     		= user,
			sueldo 			= sueldo,
			diario 			= diario,
			Gasto_general 	= gasto_general,
			date_start		=	date_start,
		)

		plan_obj.save()

		return validated_data








