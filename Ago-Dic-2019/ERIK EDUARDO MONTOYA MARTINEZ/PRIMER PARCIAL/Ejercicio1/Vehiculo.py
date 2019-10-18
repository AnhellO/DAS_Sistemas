from abc import ABCMeta, abstractmethod

class Vehiculo(metaclass=ABCMeta):
    @abstractmethod
    def traslado(self):
        pass

class Automovil(Vehiculo):

    def __init__(self, tipo, marca, modelo):
            self._tipo=tipo
            self._marca=marca
            self.modelo=modelo

    def traslado(self):
            return 'Estas viajando de manera terrestre'
    def __str__(self):
            return "Tipo: {}\nMarca: {}\nModelo: {}\n".format(self._tipo, self._marca, self.modelo).strip()

class Avion(Vehiculo):

    def __init__(self, tipo, marca, modelo):
            self._tipo=tipo
            self._marca=marca
            self._modelo=modelo

    def traslado(self):
            return 'Usted esta viajando de manera Aerea'

    def __str__(self):
            return "Tipo: {}\nMarca: {}\nModelo: {}\n".format(self._tipo, self._marca, self._modelo).strip()
class Barco(Vehiculo):

    def __init__(self, tipo, marca, modelo):
            self._tipo=tipo
            self._marca=marca
            self._modelo=modelo

    def traslado(self):
            return print('Usted viaja de manera maritima')

    def __str__(self):
            return "Tipo: {}\nMarca: {}\nModelo: {}\n".format(self._tipo, self._marca, self._modelo).strip()

def main():

    auto1 = Automovil(tipo='Carro',marca='Vw', modelo='GTI')
    print(auto1)
    avion1=Avion(
    tipo= 'Boeing', marca = 'AeroMexico', modelo='F1250')
    print(avion1)
    barco=Barco(tipo= 'Crucero', marca = 'Disney', modelo='MM20')
    print(barco)
    auto2 = Automovil(tipo='Autobus', marca='Ado', modelo='W1520')
    print(auto2)
    avion2 = Avion(tipo='Jet', marca='Interjet', modelo='Aslok')
    print(avion2)

if __name__ == '__main__':
    main()