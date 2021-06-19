import random

class Vehiculo:

    random = random.randint(1, 10)

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
      self.velocidad_maxima = velocidad_maxima
      self.kilometraje = kilometraje
      self.capacidad = capacidad

    def __str__(self):
        return " Velocidad Máxima: {} km/h, Kilometraje: {} km,  Capacidad: {} ".format(self.velocidad_maxima,self.kilometraje,self.capacidad)

class Autobus(Vehiculo):

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        Vehiculo.__init__(self, velocidad_maxima, kilometraje, capacidad)

    def __str__(self):
        return Vehiculo.__str__(self) 
 
    def tarifa(self):
        tarifa_t= self.capacidad * 100 
        monto_final= tarifa_t * 1.1
        print(f"Tarifa total -> ${monto_final}")

if __name__ == "__main__":

    lista=[
        Vehiculo (200,120000,4),
        Autobus (150,140000,10),
        Autobus (200,190000,15),
        Vehiculo (150,120000,2),
        Autobus (200,19000,20),
        Vehiculo (120,200000,4),
        Vehiculo (220,210000,2),
        Autobus (120,200000,30),
        ]

    for medio in lista:
        if isinstance(medio, Autobus):
            print(f"Soy un autobús! -> {medio}")
            medio.tarifa()
            