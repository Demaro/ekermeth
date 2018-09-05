from cuentas.models import User, Contacto
from rest_framework.authtoken.models import Token
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
from products.models import Producto, Categoria
from cuentas.api.serializers import UsuarioSerializer


class CategorySerializer(ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('id','name',)


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


class ProductCrearSerializer(ModelSerializer):
	#name = serializers.EmailField(validators=[UniqueValidator(queryset=Producto.objects.all(),
	#message="Ya existe un producto con este correo", )])
	#email2 = EmailField(label = 'Confirm Email')
	class Meta:
		model = Producto
		fields = [
			'name',
			'description',
			'categoria',
			'url_image',
			'user',
			'precio'

		]

	def create(self, validated_data):
		name = validated_data['name']
		description = validated_data['description']
		user = validated_data['user']
		categoria = validated_data['categoria']
		url_image = validated_data['url_image']
		precio = validated_data['precio']
		product_obj = Producto(
			name = name,
			description = description,
			categoria = categoria,
			url_image = url_image,
			user     = user,
			precio = precio
		)

		product_obj.save()

		return validated_data





