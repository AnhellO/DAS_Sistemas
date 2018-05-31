from django.db import models

# Create your models here.
class Sucursal(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.nombre)

class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	email = models.CharField(max_length=50)
	hotel_hospedaje = models.ForeignKey(Sucursal, null=True, blank=True, on_delete=models.CASCADE)
	habitacion = models.CharField(max_length=50)
