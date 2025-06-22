from rest_framework.permissions import BasePermission, SAFE_METHODS

"""
Este CODIGO ES SOLAMENTE PARA QUE USUARIOS SI SON ADMINS puedan obtener 
las listas de todos los usuarios, eliminar o editar todos los usuarios
O para que un usuario solamente pueda editar su propia informacion 
"""


class MiUsuario(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Permite a superusuarios/staff cualquier acción
        if request.user.is_superuser or request.user.is_staff:
            return True
            
        # Permite al dueño de su propia cuenta cualquier acción
        return obj.id == request.user.id
