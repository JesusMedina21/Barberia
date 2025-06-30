from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxLengthValidator, MinLengthValidator
from slugify import slugify
from django.db.models.signals import post_save
import requests
from django.conf import settings

activatecampaign_url  = settings.ACTIVATE_CAMPAIGN_URL
activatecampaign_key  = settings.ACTIVATE_CAMPAIGN_KEY

from djoser.signals import user_registered

import uuid,json
import requests

#from configuracion.producer import producer

import re

import uuid

pattern_special_characters = r'\badmin\b|[!@#$%^&*()_+\-={}[\]|;:",.<>?/|\s]'

def user_profile_directory_path(instance, filename):
    profile_pic_name = 'users/{0}/profile.jpg'.format(str(uuid.uuid4()))


def user_banner_directory_path(instance, filename):
    banner_pic_name = 'users/{0}/banner.jpg'.format(str(uuid.uuid4()))

class UserAccountManager(BaseUserManager):

    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)

        # Asegurarse de que el username existe antes de crear el slug
        if 'username' not in extra_fields:
            raise ValueError('Username is required')
            
        username = extra_fields['username']

        def create_slug(username):
            if re.search(pattern_special_characters, username):
                raise ValueError('Username contains invalid characters')
            username = re.sub(pattern_special_characters, '', username)
            return slugify(username)
        slug = create_slug(username)
        if not slug:
            # Si el slug está vacío, usar parte del email o un UUID
            slug = slugify(email.split('@')[0]) or str(uuid.uuid4())[:8]

        extra_fields['slug']= create_slug(extra_fields['username'])

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)



        ##Exactamente este codigo es el que hace la magia que se mande la informacion al carrito
        ##El archivo producer del monolito user manda la informacion y el consumer del carrito
        ##Recibe el uuid del usuario en el carrito, asi funciona el microservicio
        ##Es decir guarda 1 usuario en 1 base de datos y esa informacion la comparte a otra base de datos

        # Envía el evento de creación de usuario a RabbitMQ
        from configuracion.producer import send_user_registered_event
        send_user_registered_event(user)

        return user 

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.role="admin"
        user.verified=True
        user.become_seller=True
        user.save(using=self._db)

        return user
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generar slug si no existe
            if not self.username:
                raise ValueError('Username is required to generate slug')
                
            slug = slugify(self.username)
            if not slug:
                # Fallback si el slug está vacío
                slug = slugify(self.email.split('@')[0]) or str(uuid.uuid4())[:8]
            
            # Asegurarse de que el slug sea único
            original_slug = slug
            counter = 1
            while User.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f'{original_slug}-{counter}'
                counter += 1
                
            self.slug = slug
            
        super().save(*args, **kwargs)
    
class User(AbstractBaseUser, PermissionsMixin):
    roles = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    role = models.CharField(max_length=10, choices=roles, default='admin')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email
