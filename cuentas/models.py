from django.db import models
from django.contrib.auth.models import User

# Importaciones para generar token de autenticacion automaticamente
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.db import models
from cuentas.models import User
from django.core.mail import send_mail
from django.db.models import signals
from django.core.mail import EmailMessage
from plan_mensual.models import Plan_mensual



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_palan(sender, instance=None, created=False, **kwargs):
    if created:
        obj = Plan_mensual.objects.create(user=instance)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_email_register(sender, instance, **kwargs):
    name = instance.first_name
    email = instance.email

    #Enviado a mi correo:
    contact = send_mail(name + '. by: '+ email, 'Usuario registrado!: ' + name + '\n' + '\n',  ['demaromail@gmail.com',] )
    #Enviado al emisor:
    contact2 = send_mail('Gracias por unirte a ekermet! :D', 'Recibido! <3', 'demaromail@gmail.com', [email] )


class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fono = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name



def send_email(sender, instance, **kwargs):
    name = instance.name
    email = instance.email
    fono = instance.fono
    company = instance.company
    message = instance.message


    #Enviado a mi correo:
    contact = send_mail(name + '. by: '+ email, message + '\n' + '\n' + 'compañia: ' + company ,email, ['demaromail@gmail.com',] )
    #Enviado al emisor:
    contact2 = send_mail('Gracias por tu Mensaje! :D', 'Recibido! <3', 'demaromail@gmail.com', [email] )


signals.post_save.connect(send_email, sender=Contacto)



