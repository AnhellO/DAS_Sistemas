from Especial.Ejercicio1.Vehiculo import *


class Autobus(vehicle):
  def __str__(self):
    return "Corro a: {} km/h \n Tengo {}km recorridos\n y llevo hasta: {} pasajeros\n".format(self.velocidad_maxima, self.kilometraje, self.capacidad).strip()


