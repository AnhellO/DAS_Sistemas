import abc
from abc import ABCMeta

class Vehiculo(object):
    __metaclass__=ABCMeta

    @abc.abstractmethod
    def translado(self):
        print "Soy un vehiculo y me estoy trasladando"

    def getColor(self):
        pass

    def setColor(self,value):
        pass

    def __str__(self):
        return 'from new __str__: '+object.__str__(self)

    color=abc.abstractproperty(getColor,setColor)

class Auto(Vehiculo):

    def __init__(self):
        Vehiculo.__init__(self)
        self._color="azul"

    def translado(self):
        print "Soy un automovil y voy por la carretera"

    def __str__(self):
        return 'from new __str__: '+object.__str__(self)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color=value


class Avion(Vehiculo):

    def __init__(self):
        Vehiculo.__init__(self)
        self._color="azul"

    def translado(self):
        print "Soy un avion y voy por el cielo"

    def __str__(self):
        return 'from new __str__: '+object.__str__(self)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color=value

class Barco(Vehiculo):

    def __init__(self):
        Vehiculo.__init__(self)
        self._color="azul"

    def translado(self):
        print "Soy un barco y voy por el mar"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color=value


if __name__ == '__main__':

    lista_colores=['rojo','azul','verde','morado','amarillo']

    lista_autos=[]
    lista_aviones=[]
    lista_barcos=[]

    auto= Auto()
    avion=Avion()
    barco=Barco()



    print('\n *** OBJETOS AUTO *********\n')
    for x in range(0,5):
        auto.color=lista_colores[x]
        auto.translado()
        print "mi color es",auto.color
        print(auto.__str__())
        lista_autos.append(auto)

    print('\n *** OBJETOS AVION *********\n')
    for x in range(0,5):
        avion.color=lista_colores[x]
        avion.translado()
        print "mi color es",avion.color
        print(avion.__str__())
        lista_aviones.append(avion)

    print('\n *** OBJETOS BARCO *********\n')
    for x in range(0,5):
        barco.color=lista_colores[x]
        barco.translado()
        print "mi color es",barco.color
        print(barco.__str__())
        lista_barcos.append(barco)

    lista_vehiculos=[]
    for x in lista_autos:
        lista_vehiculos.append(x)


    for x in lista_aviones:
        lista_vehiculos.append(x)


    for x in lista_barcos:
        lista_vehiculos.append(x)

    lista_filtrados=[]

    def filtrar(lista_vehiculos, vehiculo_filtro):
        for x in lista_vehiculos:
            r=str(type(x))
            if vehiculo_filtro in r:
                lista_filtrados.append(x)
        return lista_filtrados

    vehiculo_filtro='Auto'
    print("\n ***Se han filtrado los {} *********".format(vehiculo_filtro))
    filtro=filtrar(lista_vehiculos,vehiculo_filtro)

    for x in filtro:
        print x.__str__()

# avion= Avion()
# avion.color="Azul"
# avion.translado()
# print "mi color es",avion.color
# print(avion.__str__())
#
# barco= Barco()
# barco.color="Azul"
# barco.translado()
# print "mi color es",barco.color
# print(barco.__str__())
