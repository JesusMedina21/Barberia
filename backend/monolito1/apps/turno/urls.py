from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include, re_path
from apps.turno.views import *
from apps.turno import views

urlpatterns=[
    
]

if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)