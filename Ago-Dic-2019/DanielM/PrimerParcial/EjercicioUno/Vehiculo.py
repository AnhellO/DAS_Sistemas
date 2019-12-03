# Ejercicio 1 - OOP Basics

from abc import ABCMeta, abstractmethod

class Vehiculo(metaclass=ABCMeta):
    @abstractmethod
    def traslado(self):
        pass

    def __str__(self):
        return ""


class Automovil(Vehiculo):
    def __init__(self, Color, Brand, Displace, MedVel):
        self._color = Color
        self._marca = Brand
        self._desplazamiento = Displace
        self._vel = MedVel

    def traslado(self):
        return f'Funciono con gasolina verde o roja :v.'

    def getDesplazamiento(self):
        return self._desplazamiento

    def __str__(self):
        return f"Manejo un Automóvil color {self._color}, que es marca {self._marca}, este es un tipo de " \
               f"Vehículo {self._desplazamiento} y su velocidad es medida en {self._vel} "


class Avion(Vehiculo):
    def __init__(self, Airline, Brand, Displace, MedVel):
        self._aerolinea = Airline
        self._marca = Brand
        self._desplazamiento = Displace
        self._vel = MedVel

    def traslado(self):
        return f'Funciono con un combustible llamado avtur.'

    def getDesplazamiento(self):
        return self._desplazamiento

    def __str__(self):
        return f"Viajo en un Avión de la aerolínea {self._aerolinea}, su marca es {self._marca}, este es un tipo de " \
               f"Vehículo {self._desplazamiento} y su velocidad es medida en {self._vel} "


class Barco(Vehiculo):
    def __init__(self, tipo, destino, Displace, MedVel):
        self._tipo = tipo
        self._destino = destino
        self._desplazamiento = Displace
        self._vel = MedVel

    def traslado(self):
        return f'Funciono con fuelóleo.'

    def getDesplazamiento(self):
        return self._desplazamiento

    def __str__(self):
        return f"Estoy navegando en un Barco de tipo {self._tipo}, con destino a {self._destino}, este es un tipo de " \
               f"Vehículo {self._desplazamiento} y su velocidad se mide en {self._vel} "


def validar(vehiculos, desplazamiento):
    vehiculosFiltrados = []
    for i in vehiculos:
        if i.getDesplazamiento() == desplazamiento:
            vehiculosFiltrados.append(i)

    return vehiculosFiltrados


def main():
    automovil1 = Automovil('Naranja', 'Chevrolet', 'terrestre', 'km.')
    automovil2 = Automovil('Negro Mate', 'Ford', 'terrestre', 'KM.')
    avion1 = Avion('Viva Aerobus', 'Boeing', 'aéreo', 'nudos.')
    avion2 = Avion('Magni', 'Airbus', 'aéreo', 'Nudos.')
    barco1 = Barco('Crucero', 'Europa', 'marítimo', 'millas náuticas.')

    print(f'{automovil1}\n{automovil2}\n{avion1}\n{avion2}\n{barco1}')

    vehiculos = [automovil1, avion1, barco1, automovil2, avion2]
    desplazamiento = 'aéreo'
    print(validar(vehiculos, desplazamiento))


if __name__ == '__main__':
    main()
