import random
class Vehiculo(object):    
    random = random.randint(1,1000)

    def __init__(self,velocidad_maxima,kilometraje,capacidad):
        self._velocidad_maxima = velocidad_maxima
        self._kilometraje = kilometraje
        self._capacidad = capacidad

    def __str__(self):
        return f"La velocidad maxima es de: {self._velocidad_maxima} km/h\nEl kilometraje es de: {self._kilometraje} km\nLa capacidad es de {self._capacidad} asientos"

    def tarifa(self):
        asientos = self._capacidad 
        tarifa_vehiculo = asientos * 100
        return tarifa_vehiculo

class Autobus(Vehiculo):
    def __init__(self,velocidad_maxima,kilometraje,capacidad):
        Vehiculo.__init__(self,velocidad_maxima,kilometraje,capacidad)


if __name__=="__main__":
    l_vehiculos = [Vehiculo(120,100000,5),Vehiculo(150,54785,2),Autobus(120,58746,46),Vehiculo(280,0,5),Autobus(120,47856,40)]

    for vehiculo in l_vehiculos:
        if isinstance(vehiculo,Autobus):
            cargo_mantenimiento = vehiculo.tarifa() * .10
            tarifa_total = vehiculo.tarifa() + cargo_mantenimiento
            print (f"Soy un autobus! -> {vehiculo}")