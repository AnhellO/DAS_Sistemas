from abc import ABCMeta, abstractmethod
class Vehiculo(metaclass=ABCMeta):
    @abstractmethod
    def traslado(self):
        pass

    def __str__(self):
        return ""

class Automovil(Vehiculo):
    def __init__(self, color, marca, desplasamiento, medicionVelocidad):
        self._color = color
        self._marca = marca
        self._desplasamiento = desplasamiento
        self._medicionVelocidad = medicionVelocidad

    def traslado(self):
        return f'Yo te muevo usando Gasolina!!!'

    def getDesplasamiento(self):
        return self._desplasamiento

    def __str__(self):
        return f"Yo me muevo en un Automovil color {self._color}, de la marca {self._marca}, es un Vehiculo {self._desplasamiento} y su velocidad se mide en {self._medicionVelocidad}"

class Avion(Vehiculo):
    def __init__(self, compania , marca, desplasamiento, medicionVeolocidad):
        self._compania = compania
        self._marca = marca
        self._desplasamiento = desplasamiento
        self._medicionVelocidad = medicionVeolocidad

    def traslado(self):
        return f'Yo te muevo usando Gasolina para Aviones!!!'

    def getDesplasamiento(self):
        return self._desplasamiento

    def __str__(self):
        return f"Yo me muevo en un Avion de la compañia {self._compania}, de la marca {self._marca}, es un Vehiculo {self._desplasamiento} y su velocidad se mide en {self._medicionVelocidad}"

class Barco(Vehiculo):
    def __init__(self, tipo, destino, desplasamiento, medicionVelocidad):
        self._tipo = tipo
        self._destino = destino
        self._desplasamiento = desplasamiento
        self._medicionVelocidad = medicionVelocidad

    def traslado(self):
        return f'Yo te muevo usando Gasolina para Barcos!!!'

    def getDesplasamiento(self):
        return self._desplasamiento

    def __str__(self):
        return f"Yo me muevo en un Barco de tipo {self._tipo}, con destino a {self._destino }, es un Vehiculo {self._desplasamiento} y su velocidad se mide en {self._medicionVelocidad}"


def validar(vehiculos, desplasamiento):
    vehiculosFiltrados = []
    for i in vehiculos:
        if i.getDesplasamiento() == desplasamiento:
            vehiculosFiltrados.append(i)

    return vehiculosFiltrados

def main():
    automovil1 = Automovil('rojo', 'Jeep', 'terrestre', 'kilometros')
    avion1 = Avion('volaris', 'McDonnell Douglas MD-80', 'aéreo', 'kilometros aéreos')
    barco1 = Barco('Placer', 'Hawai', 'marítimo', 'nudos')
    avion2 = Avion('turi-mexico', 'Indonesia', 'aéreo', 'kilometros turbo aéreos')
    automovil2 = Automovil('patriotico', 'Mustang', 'terrestre', 'millas gringas')
    print(f'{automovil1}\n{avion1}\n{barco1}\n{avion2}\n{automovil2}')
    vehiculos = [automovil1, avion1, barco1, automovil2, avion2]
    desplasamiento = 'aéreo'
    print(validar(vehiculos, desplasamiento))

if __name__== '__main__':
    main()