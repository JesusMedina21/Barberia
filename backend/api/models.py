from django.db import models
# from django.contrib.auth.models import User # Modelo original
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    #aqui modifico el username para que sea obligatorio pero no unico, 
    #es decir que pueda registrar varios usuarios con el mismo nombre pero no con el mismo correo
    username = models.CharField(max_length=150, unique=False, blank=False, null=False)
    #aqui tengo que indicar por exigencias de Django, que al nombre ya no ser unico
    #lo que va a identificar el usuario como ID seria el email, por lo tanto tengo que
    #sobreescribir el campo email e identificar el email en USERNAME_FIELD y colocar el
    #REQUIRED_FIELDS a juro porque sino, el codigo no va a funcionar por exigencias del framework
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 
    
    class Meta:
        # Asegúrate de que no haya restricciones de unicidad
        unique_together = ()  

