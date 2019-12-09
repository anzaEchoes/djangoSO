from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
from polls import views
from django.contrib import admin

urlpatterns = [
	re_path(r'^listadealumnos/$', views.ListaAlumnos.as_view() ),
    re_path(r'^detallesdelalumno/(?P<id>\d+)$', views.AlumnosDetalles.as_view() ),
    re_path(r'^listadecarreras/$', views.CarreraLista.as_view() ),
    re_path(r'^detallesdecarrera/(?P<id>\d+)$', views.CarreraDetalles.as_view() ),

    path('rest-auth/', include('rest_auth.urls')),
	#path('', views.index, name = 'index'),
	#path('', views.IniciarSesion, name = 'iniciarsesion'),
]