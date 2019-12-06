from django.db import models

# Create your models here.
class Carrera(models.Model):        
    nombre_carrera = models.CharField(max_length=60)
    delet = models.BooleanField(default = False)

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField(default=0)
	sexo = models.CharField(max_length=30)
	direccion = models.CharField(max_length=200)
	carrera = models.CharField(max_length=100)
	carrera = models.ForeignKey(Carrera, related_name='alumno', on_delete=models.CASCADE)#null=false
    #delet = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre
