import random
class vehiculo(object):
    random = random.randint(1,100)
    def __init__(self,velocidad_maxima,kilometraje,capacidad):
        self.vel_max = velocidad_maxima
        self.kilo = kilometraje
        self.cap = capacidad
    def tarifa(self):
        asientos = self.cap
        tarifa_vehiculo = asientos * 100
        return tarifa_vehiculo
    def __str__(self):
        return f"Velocidad maxima: {self.vel_max} km/h\nKilometraje: {self.kilo} km\nCapacidad: {self.cap}"

class autobus(vehiculo):
    def __init__(self,vel_max,kilo,cap):
        vehiculo.__init__(self,vel_max,kilo,cap)

if __name__=="__main__":
    vehiculos = [vehiculo(180,12000,5),vehiculo(160,89761,4),autobus(110,6000,40),vehiculo(200,100,5),autobus(120,3800,40)]
    #Ciclo para iterar la lista
    for vehiculo in vehiculos:
        if isinstance(vehiculo,autobus):
            mantenimiento = vehiculo.tarifa() * .10
            tarifa_total = vehiculo.tarifa() + mantenimiento
            print (f"Soy un autobus! -> {vehiculo}")
