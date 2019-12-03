import abc

#   Crea una clase base abstracta Vehiculo. De esta clase heredarán las clases Automovil, Avion y Barco:
#       - Agrega la función abstracta traslado() en la clase Vehiculo y sobreescribela en cada una las clases hijas con una funcionalidad específica
#       - Para cada clase sobreescribe la función __str__, de tal manera que podamos obtener una representación del objeto como string
#       - Crea la función main en la cual instancies y juegues con al menos 5 objetos diferentes (en total) para cada una de las clases pedidas anteriormente
#       - Crea una función dentro de tu test principal la cual reciba como parámetros una lista de objetos tipo vehículo y un tipo en específico 
#         (ya sea 'marítimo', 'terrestre' o 'aéreo'), y devuelva una nueva lista filtrada con los objetos del tipo especificado en el segundo parámetro
from abc import ABCMeta
class Vehiculo(object):
    #Clase Vehiculo
    @abc.abstractmethod
    def traslado(self):
        pass

class Automovil(Vehiculo):
    def __init__(self, funicion, tipo):
        self.funcion = funicion
        self.tipo = tipo
    def traslado(self):
        return self.funcion
    def getTipo(self):
        return self.tipo
    def __str__(self):
        cadena = "Soy un Carro y mi funcion es: {}".format(self.traslado())
        return cadena
class Avion(Vehiculo):
    def __init__(self, funcion, tipo):
        self.funcion = funcion
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def traslado(self):
        return self.funcion
    def __str__(self):
        cadena = "Soy un Avion y mi funcion es: {}".format(self.traslado())
        return cadena
class Barco(Vehiculo):
    def __init__(self, funcion,tipo):
        self.funcion = funcion
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def traslado(self):
        return self.funcion
    def __str__(self):
        cadena = "Soy un Barco y mi funcion es: {}".format(self.traslado())
        return cadena
def filtro(trasnportes, tipo):
    vehiculosEnFIltro = []
    for i in trasnportes:
        if i.getTipo() == tipo:
            vehiculosEnFIltro.append(i)
    return vehiculosEnFIltro
def main():
    auto1 = Automovil("Llevar gente a distancias largas", "terrestre")
    print(auto1)
    auto2 = Automovil("Reducir tiempos de trayectos", "terrestre")
    print(auto2)
    avion = Avion("Llevar a otros paises", "aereo")
    print(avion)
    barco1 = Barco("Transportar contenedores con distintos productos de un pais a otro", "maritimo")
    print(barco1)
    barco2 = Barco("Servir como buque de pasajeros para cruceros", "maritimo")
    print(barco2)

    transportes = [auto1, auto2, avion, barco1, barco2]
    tipo = 'aereo'
    lista = filtro(transportes, tipo)
    print(lista[0])
if __name__ == '__main__':
    main()