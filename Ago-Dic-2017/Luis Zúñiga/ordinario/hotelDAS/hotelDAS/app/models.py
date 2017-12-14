"""
Definition of models.
"""

from django.db import models

# Create your models here.

# Modela la información de un cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length = 50)
    paterno = models.CharField(max_length = 50)
    materno = models.CharField(max_length = 50)
    edad = models.PositiveIntegerField()
    email = models.EmailField()
    direccion = models.TextField()
    tcredito = models.PositiveIntegerField(primary_key=True)

# Modela un hotel
class Hotel(models.Model):
    idHotel = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    direccion = models.TextField()
    estrellas = models.IntegerField()

class TipoHabitacion(models.Model):
    tipo = models.IntegerField(primary_key = True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# Modela una habitación
class Habitacion(models.Model):    
    tipo = models.ForeignKey('TipoHabitacion',on_delete=models.CASCADE, default = 1)
    idHotel = models.ForeignKey('Hotel',on_delete=models.CASCADE, default = 1)
    cantidad = models.PositiveIntegerField(default = 30)


# Modela una Reservación
class Reservacion(models.Model):
    numeroReservacion = models.AutoField(primary_key=True)
    totalAPagar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tcredito = models.ForeignKey('Cliente',on_delete=models.CASCADE)
    cantidadNoches  = models.PositiveIntegerField(default = 1)
