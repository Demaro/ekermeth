from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Plan_mensual(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sueldo = models.CharField(max_length=100, blank=True, null=True)
    diario = models.CharField(max_length=100, blank=True, null=True)
    gasto_general = models.ManyToManyField('Gasto_general', blank=True)
    date_start	=	models.DateTimeField(auto_now_add=True, blank=True)
    total		=	models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class Gasto_general(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(blank=True, null=True)
    #gasto_general = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name