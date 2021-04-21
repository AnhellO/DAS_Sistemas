random = 5
class Vehiculo():
    random = 5
    def __init__(self,velocidad_maxima, kilometraje, capacidad):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad
    def __str__(self):
        """Devuelve una cadena representativa del vehículo"""
        return "Velocidad: {} km/h \nTengo {} km recorridos\ny Capacidad: {} pasajeros\n".format(self.velocidad_maxima, self.kilometraje, self.capacidad)


class Autobus(Vehiculo):
    """Clase que representa a un Autobus"""
    def __init__(self, velocidad_maxima, kilometraje, capacidad):
        super().__init__(velocidad_maxima, kilometraje, capacidad)

    def __str__(self):
        return "Soy un autobús!-> Velocidad: {} km/h \nTengo {} km recorridos\ny Capacidad: {} pasajeros\n".format(self.velocidad_maxima, self.kilometraje, self.capacidad)
    
    def tarifa(self, capacidad):
        tarifa = self.capacidad*100
        tarifa_autobus = (.10 * tarifa) + tarifa
        return tarifa_autobus


def __main__():
  if __name__ =="__main__":
       au1 =  Vehiculo(150, 50000, 5)
       be1 = Autobus(200, 89560, 20)
       au2 =  Vehiculo(250, 150000, 4)
       be2 = Autobus(175, 9560, 30)
       au3 =  Vehiculo(350,7000, 2)
       be3 = Autobus(198, 7560, 15)
       vehiculos = [au1,be1,au2,be2,au3,be3]

       for i in vehiculos:
            if isinstance(i,Autobus):
                p =i.tarifa(i.capacidad)
                print(f" {i} -> La tarifa es: ${p}")
                print('''
                            ''')

__main__()
 


  



  








  