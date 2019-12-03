"""Ejercicio 1 - OOP Basics
Crea una clase base abstracta Vehiculo. De esta clase heredarán las clases Automovil, Avion y Barco:
Agrega la función abstracta traslado() en la clase Vehiculo y sobreescribela en cada una las clases hijas con una funcionalidad específica
Para cada clase sobreescribe la función __str__, de tal manera que podamos obtener una representación del objeto como string
Crea la función main en la cual instancies y juegues con al menos 5 objetos diferentes (en total) para cada una de las clases pedidas anteriormente
Crea una función dentro de tu test principal la cual reciba como parámetros una lista de objetos tipo vehículo y un tipo en específico
(ya sea 'marítimo', 'terrestre' o 'aéreo'),
y devuelva una nueva lista filtrada con los objetos del tipo especificado en el segundo parámetro"""

from abc import ABCMeta, abstractmethod
class Vehiculo(metaclass=ABCMeta):
    @abstractmethod
    def traslado(self):
        pass

    def __str__(self):
        return ""

class Automovil(Vehiculo):
    def __init__(self, color, tipo):
        self._color = color
        self._tipo = tipo

    def traslado(self):
        return f'Yo me transporto por tierra'

    def __str__(self):
        return f"Yo tengo un Automovil color {self._color}, y es un Vehiculo de tipo {self._tipo}"

class Avion(Vehiculo):
    def __init__(self, color, tipo):
        self._color = color
        self._tipo = tipo

    def traslado(self):
        return f'Yo me transporto por el aire xDD'

    def __str__(self):
        return f"Yo tengo un Avion color {self._color}, y es un Vehiculo de tipo {self._tipo}"

class Barco(Vehiculo):
    def __init__(self, color, tipo):
        self._color = color
        self._tipo = tipo

    def traslado(self):
        return f'Yo me transporto por el mar'

    def __str__(self):
        return f"Yo tengo un Barco color {self._color}, y es un Vehiculo de tipo {self._tipo}"

def validar(vehiculos, desplasamiento):
    vehiculosFiltrados = []
    for i in vehiculos:
        if i.getDesplasamiento() == desplasamiento:
            vehiculosFiltrados.append(i)

    return vehiculosFiltrados

def main():
    automovil1 = Automovil('rojo', 'terrestre')
    print(automovil1)
    avion1 = Avion('blanco','aereo')
    print(avion1)
    barco1 = Barco('azul','maritimo')
    print(barco1)
    avion2 = Avion('blanco con rojo','aereo')
    print(avion2)
    automovil2 = Automovil('dorado con bronce','terrestre')
    print(automovil2)


if __name__== '__main__':
    main()