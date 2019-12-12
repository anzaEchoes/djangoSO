from django.shortcuts import render
from datos.models import Alumno, Carrera
from datos.serializer import AlumnoSerializers, CarreraSerializers

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.permissions import IsAuthenticated  # <-- Here

class AlumnoLista(APIView):
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


class Filtrar(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        nombre=kwargs.get('nombre')
        nombre=nombre.replace('_',' ')
        try:
            apellidos=kwargs.get('apellidos')
            apellidos=apellidos.replace('_',' ')
            console.log('apellidos: '+apellidos)
            queryset= Alumno.objects.filter(nombre=nombre, apellidos=apellidos, delet=False)
        except:
            queryset= Alumno.objects.filter(nombre=nombre, delet=False)
        if len(queryset) is 0:
            try:
                carreraid= Carrera.objects.filter(nombre_carrera=nombre, delet=False).values('id')[0]['id']
                queryset= Alumno.objects.filter(carrera=carreraid, delet=False)
            except:
                queryset= Alumno.objects.filter(edad=nombre, delet=False)
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

class AlumnoDetalles(APIView):
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