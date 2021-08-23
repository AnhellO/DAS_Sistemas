import random


class Vehiculo(object):

    random = random.randrange(100)
    
    def __init__(self,vMaxima,kilometrajemetraje,capacidadacidad):
        self.vMaxima = vMaxima
        self.kilometraje = kilometrajemetraje
        self.capacidad = capacidadacidad

    def __str__(self):
        return "\nVelocidad maxima: {} km/h\nkilometros recorridos: {} km\nCapacidadacidad de transporte: {} personas".format(self.vMaxima,self.kilometraje,self.capacidad)

class Autobus(Vehiculo):
    def __init__(self,vMaxima,kilometraje,capacidad):
        Vehiculo.__init__(self,vMaxima,kilometraje,capacidad)
    
    def tarifa(self):
        asientos = self.capacidad
        tarifa_Vehiculo = asientos * 100
        return tarifa_Vehiculo

if __name__=="__main__":
    lista = [Autobus(100,12000,10),Vehiculo(160,89761,4),Vehiculo(110,6000,40),Vehiculo(200,100,5),Vehiculo(120,3800,40)]
    
    for Vehiculo in lista:
        if isinstance(Vehiculo,Autobus):
            tarifaMantenimiento = Vehiculo.tarifa() * .10
            tar = Vehiculo.tarifa() + tarifaMantenimiento
            print ("Soy un Autobus {}".format(Vehiculo))
