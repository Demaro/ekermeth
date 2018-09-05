from django.db import models
from django.conf import settings

class Producto(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True)
	precio = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True, blank=True)
	url_image = models.CharField(max_length=1000, null=True)

	
	def __str__(self):
		return self.name


class Categoria(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name



