from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from slugify import slugify
import uuid
import re
import json
import pika
import os
import logging
from django.conf import settings
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

# Configuración de RabbitMQ
def send_to_rabbitmq(user):
    """Envía el usuario a RabbitMQ para crear el carrito"""
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters(settings.CLOUDAMQP_URL))
        channel = connection.channel()
        
        channel.queue_declare(queue='user_registered', durable=True)
        
        message = {
            'id': str(user.id),
            'email': user.email,
            'username': user.username
        }
        
        channel.basic_publish(
            exchange='',
            routing_key='user_registered',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        
        connection.close()
        logger.info(f"Evento enviado para usuario {user.id}")
    except Exception as e:
        logger.error(f"Error enviando a RabbitMQ: {e}")

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    make_admin = forms.BooleanField(
        label='Is admin',
        required=False,
        help_text='Give this user all permissions'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'make_admin')

    def clean_username(self):
        """Valida el username y genera el slug"""
        username = self.cleaned_data.get('username')
        
        # Validar que el username no esté vacío
        if not username:
            raise ValidationError("Username is required")
            
        # Generar slug válido
        try:
            slug = slugify(username)
            if not slug:  # Si el slug está vacío después de slugify
                raise ValidationError("Could not generate a valid slug from username")
                
            # Verificar si el slug ya existe
            if User.objects.filter(slug=slug).exists():
                raise ValidationError("A user with a similar username already exists")
                
        except Exception as e:
            raise ValidationError(f"Error generating slug: {str(e)}")
            
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        # Generar slug desde el username
        username = self.cleaned_data.get('username')
        if username:
            user.slug = slugify(username) or f"user-{uuid.uuid4().hex[:8]}"
        
        if self.cleaned_data['make_admin']:
            user.is_staff = True
            user.is_superuser = True
            user.role = 'admin'
        
        if commit:
            try:
                user.save()
                send_to_rabbitmq(user)
            except Exception as e:
                logger.error(f"Error saving user: {e}")
                raise
        
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_slug(self):
        """Valida el slug al editar"""
        slug = self.cleaned_data.get('slug')
        if not slug:
            # Generar slug desde el username si está vacío
            username = self.cleaned_data.get('username')
            if username:
                return slugify(username) or f"user-{uuid.uuid4().hex[:8]}"
            raise ValidationError("Could not generate a valid slug")
        return slug

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 
                     'password1', 'password2', 'is_active', 'make_admin'),
        }),
    )
    
    fieldsets = (
        (None, {'fields': ('username', 'password', 'slug')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
    )
    
    def save_model(self, request, obj, form, change):
        """Sobrescribe para manejar slugs al guardar desde admin"""
        if not change:  # Solo para nuevos usuarios
            if not obj.slug:
                obj.slug = slugify(obj.username) or f"user-{uuid.uuid4().hex[:8]}"
        
        super().save_model(request, obj, form, change)
        
        if not change:
            send_to_rabbitmq(obj)

admin.site.register(User, UserAdmin)