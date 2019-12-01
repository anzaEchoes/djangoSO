from django.db import models

# Create your models here.
class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField(default=0)
	sexo = models.CharField(max_length=30)
	direccion = models.CharField(max_length=200)
	carrera = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre