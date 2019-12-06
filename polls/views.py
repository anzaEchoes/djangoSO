from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from polls.models import Alumno, Carrera
from polls.serializer import AlumnoSerializers, CarreraSerializers
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
"""class IniciarSesion(APIView):
	def get(self, request, format=None):
        queryset = Grupo.objects.filter(delete=False)
        serializer = GrupoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GrupoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def index(request):
	return HttpResponse("Hola mundo")
"""
#class AlumnoLista(APIView):
class ListaAlumnos(APIView):
    permission_classes = (IsAuthenticated,)    
    
    def get(self, request, format=None):
        queryset = Alumno.objects.filter(delet=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AlumnosDetalles(APIView):
    permission_classes = (IsAuthenticated,)    
    def get_object(self, id):
        try:
            return Alumno.objects.get(pk=id, delet=False)
        except Alumno.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = AlumnoSerializers(usuario)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumno.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        usuario = self.get_object(id)
        if usuario != False:
            serializer = AlumnoSerializers(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Carrera
class CarreraLista(APIView):
    permission_classes = (IsAuthenticated,)    
    def get(self, request, format=None):
        queryset = Carrera.objects.filter(delet=False)
        serializer = CarreraSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CarreraSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CarreraDetalles(APIView):
    permission_classes = (IsAuthenticated,)    
    def get_object(self, id):
        try:
            return Carrera.objects.get(pk=id, delet=False)
        except Carrera.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        carrera = self.get_object(id)
        if carrera != False:
            serializer = CarreraSerializers(carrera)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Carrera.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        denuncia = self.get_object(id)
        if denuncia != False:
            serializer = CarreraSerializers(denuncia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)