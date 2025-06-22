from rest_framework import serializers
# from django.contrib.auth.models import User # Modelo original
from apps.user.models import *

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from decimal import Decimal

from rest_framework.response import Response
from rest_framework.exceptions import APIException

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    # estos son los campos que quiero que se conviertan a json
        #fields = ['id', 'username', 'email', 'password']
        fields = ['id', 'username', 'email', 'password']
    #Validacion para no colocar campos adicionales en peticion POST/PATCH en herramientas como Postman
    def validate(self, data):
        model_fields = {field.name for field in User._meta.get_fields()}
        extra_fields = set(self.initial_data.keys()) - model_fields
        
        if extra_fields:
            raise serializers.ValidationError(
                f"Campos no permitidos: {', '.join(extra_fields)}. "
                f"Campos válidos: {', '.join(model_fields)}"
            )
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        User = get_user_model()  # Obtiene el modelo de usuario actual
        try:
            user = User.objects.get(email=email)  # Busca el usuario por email
        except User.DoesNotExist:
            raise serializers.ValidationError(_('Invalid email or password.'))
        if not user.check_password(password):  # Verifica la contraseña
            raise serializers.ValidationError(_('Invalid email or password.'))
        
        attrs['user'] = user
        return attrs
    
# Nuevo serializador para el refresh token
class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()