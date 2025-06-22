from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include, re_path
from apps.user.views import *
from apps.user import views

#DRF SPECTACULAR 

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.utils import extend_schema_view, extend_schema

#REDIRECCIONAMINENTO

from django.views.generic.base import RedirectView



@extend_schema_view(
    get=extend_schema(exclude=True)  # <- esto la excluye de Swagger
)
class HiddenSchemaView(SpectacularAPIView):
    pass


router=routers.DefaultRouter()
router.register(r'user', views.UserViewSet)   #endpoint 

urlpatterns=[
    path('', include(router.urls)),
    #swagger
    path('docs/', SpectacularSwaggerView.as_view(), name='docs'),
    #DRF SPECTACULAR SIN EL SCHEMA NO FUNCIONA DOCS
    path('schema/', HiddenSchemaView.as_view(),name='schema'),
    #DRF JWT
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #REDIRECCOINAMIENTO
    re_path(r'^(?!api/docs/).*$', RedirectView.as_view(url='/admin/', permanent=False)),
    re_path('', RedirectView.as_view(url='docs/', permanent=False)),
]
if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)