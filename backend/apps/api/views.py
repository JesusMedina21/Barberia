from rest_framework import viewsets, status, generics
from apps.api.serializers import *

# from django.contrib.auth.models import User # Modelo original
from apps.api.models import *
# JWT
from rest_framework.permissions import IsAuthenticated, AllowAny

#DRF SPECTACULAR
from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework.decorators import action
from rest_framework.response import Response

from apps.api.permissions import *

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView as BaseTokenRefreshView



@extend_schema(tags=['Token'], request=RefreshTokenSerializer)
class TokenRefreshView(generics.GenericAPIView):
    serializer_class = RefreshTokenSerializer  # 👈 Serializador creado manualmente


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = serializer.validated_data.get('refresh')

        if refresh:
            try:
                token = RefreshToken(refresh)
                access_token = token.access_token
                return Response({'access': str(access_token)}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': 'Token inválido'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Se requiere el token de refresco'}, status=status.HTTP_400_BAD_REQUEST)



@extend_schema(tags=['Login'])
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Generar tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

###################################3333333#USER###############################################

@extend_schema_view(
    list=extend_schema(tags=['User']),
    retrieve=extend_schema(tags=['User']),
    create=extend_schema(exclude=True),  # Excluye el create genérico
    methods=['POST'], tags=['User'], 
    update=extend_schema(exclude=True),  # Oculta el método PUT (update)
    partial_update=extend_schema(tags=['User']),
    destroy=extend_schema(tags=['User']),
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.action == 'list':
            # Solo admin puede listar todos los usuarios
            if self.request.user.is_staff:
                return User.objects.all()
            return User.objects.filter(id=self.request.user.id)
        return super().get_queryset()


    def get_permissions(self):
        if self.action == 'register': # Esta linea significa que el endpoint register lo pueda usar cualquiera
            return [AllowAny()]  # Permitir registro sin autenticación
        elif self.action in ['retrieve', 'partial_update', 'destroy']:  
            # Permitir acceso a retrieve, update y destroy solo si el usuario está autenticado
           
            # Y que el resto de metodos usen IsAuthenticated que significa JWT y el IsSelf que significa
            # que el mismo usuario pueda acceder a su propio recurso, ejemplo el usuario 1 solo acceda al endpoint 1 
            return [IsAuthenticated(), MiUsuario()]  # 👈 Requiere autenticación y que sea el mismo usuario 
        #El IsAuthenticated es creado automaticamente por Django, MiUsuario es creado manualmente
        return [IsAuthenticated()]
    
    @extend_schema(exclude=True)  # 👈 Oculta este método del esquema Swagger
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Método no permitido. Usa /api/user/register/."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(description="Registro de nuevos usuarios", tags=['User']) 
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Crear usuario con contraseña hasheada
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
   
    def update(self, request, *args, **kwargs):
        if not kwargs.get('partial', False):
            return Response(
                {"detail": "Método PUT no permitido. Use PATCH en su lugar."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs) 
