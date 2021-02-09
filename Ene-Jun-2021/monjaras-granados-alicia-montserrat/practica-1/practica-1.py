import random
# Clase base.
class Vehiculo:

    random = random.randint(10, 20)

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
      self.velocidad_maxima = velocidad_maxima
      self.kilometraje = kilometraje
      self.capacidad = capacidad

    def __str__(self) -> str:
        return " Velocidad Máxima: {} km/h, Kilometraje: {} km,  Capacidad: {} ".format(self.velocidad_maxima,self.kilometraje,self.capacidad)
# Clase hija que hereda a Vehículo
class Autobus(Vehiculo):

    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        Vehiculo.__init__(self, velocidad_maxima, kilometraje, capacidad)

    def __str__(self):
        return Vehiculo.__str__(self) 
    # Método que obtiene la tarifa total por instancia del autobús.
    def tarifa(self):
        tarifa_total = self.capacidad * 100 
        monto_final = tarifa_total + (tarifa_total*.10)
        print(f"Tarifa total -> ${monto_final}")
  
if __name__ == "__main__":

    lista_transportes = [
        Vehiculo (120 ,150, 6),
        Vehiculo(80, 100, 6),
        Autobus(110,1550,25),
        Vehiculo(200, 1200,4),
        Autobus(100, 900,15),
        Vehiculo(100,1600,2),
        Autobus(90, 100, 18),
        Vehiculo(105,1516,4),
        Autobus( 80, 300, 20),
    ]
    
    # Ciclo que itera en la lista__transportes para determinar si es una instancia de la clase Autobús
    for medio_transporte in lista_transportes:
        if isinstance(medio_transporte, Autobus):
            print(f"Soy un autobús! -> {medio_transporte}")
            medio_transporte.tarifa()

    

   