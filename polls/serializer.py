from rest_framework import routers, serializers, viewsets
from polls.models import Alumno, Carrera


class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        carreras = serializers.SlugRelatedField(many=True,read_only=True,slug_field='alumnos')
        model = Alumno
        fields = ('__all__')

class CarreraSerializers(serializers.ModelSerializer):
    nombreAlumno =serializers.ReadOnlyField(source='re_carrera.nombre')
    apellidosAlumno=serializers.ReadOnlyField(source='re_carrera.apellidos')
    class Meta:
        model = Carrera
        fields = ('__all__')