import random
#Clase vehiculo
class vehiculo():
    random.randint(0, 5)
    def __init__(self, velocidad_maxima, kilometrage, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometrage = kilometrage
        self.capacidad = capacidad
    
    def __str__(self):
        return f"Velocidad maxima: {self.velocidad_maxima}  Kilometraje: {self.kilometrage} Capacidad: {self.capacidad}"

class autobuss(vehiculo):

    def __init__(self, velocidad_maxima, kilometrage, capacidad):
        super().__init__( velocidad_maxima, kilometrage, capacidad)
    
    def tarifa(self):
        tarifa_predeterminada = self.capacidad * 100
        monto_final = tarifa_predeterminada + (tarifa_predeterminada * 0.1)
        print("tarifa total: ", monto_final)

if __name__ == "__main__":

    test = [ vehiculo(120, 1000, 4), autobuss(80, 5000, 18), vehiculo(210, 9999, 4), autobuss(120, 1000, 24)]

    for a in test:
        if isinstance(a,vehiculo):
            print(f"Soy un autobús! -> {a}")