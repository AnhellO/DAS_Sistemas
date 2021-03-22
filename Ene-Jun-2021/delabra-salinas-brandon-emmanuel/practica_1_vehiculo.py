import random as rnn

# clase vehiculo
class vehiculo:

    Random = 60

    def __init__(self, velocidad_maxima, kilometraje, capacidad):

        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje
        self.capacidad = capacidad

#funcion tarifa
    def tarifa(self,asientos: int = 20):

        tarifa_inicial= asientos*100
        return tarifa_inicial


    def __str__(self)->str :

        return f'La velocidad maxima es de {self.velocidad_maxima} km/h\n' \
               f'El kilometraje es de {self.kilometraje}\n' \
               f'Con una capacidad de {self.capacidad} pasajeros'

#clase autobus 
class autobus(vehiculo):

    def __init__(self,velocidad_maxima,kilometraje,capacidad):
        vehiculo.__init__(self,velocidad_maxima,kilometraje,capacidad)


if __name__=="__main__":


        
    lista_vehiculo = [
        vehiculo(120, 180, 5),
        autobus(150, 200, 50),
        vehiculo(90, 100, 10),
        autobus(105, 800, 65)
       ]

    for i in lista_vehiculo:

        if isinstance(i,autobus):
            inicial = i.tarifa()*.10
            tarifa_final = i.tarifa() + inicial
            print(f"Soy un autobus! -> {i}, mi tarifa total es {tarifa_final}")    
            
       



       