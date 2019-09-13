import time

class EstacionDeRadio:
    _frecuencia = None

    def __init__(self, frecuencia):
        self._frecuencia = frecuencia

    def getFrecuencia(self):
        return self._frecuencia

class Estaciones:
    _estaciones = []

    def agregarEstacion(self, estacion):
        self._estaciones.append(estacion)

    def getEstaciones(self):
        return [estacion.getFrecuencia() for estacion in self._estaciones]

if __name__ == '__main__':
    contenedorEstaciones = Estaciones()

    estacion1 = EstacionDeRadio(89.9)
    estacion2 = EstacionDeRadio(101.2)
    estacion3 = EstacionDeRadio(102.3)
    estacion4 = EstacionDeRadio(100.4)

    contenedorEstaciones.agregarEstacion(estacion1)
    contenedorEstaciones.agregarEstacion(estacion2)
    contenedorEstaciones.agregarEstacion(estacion3)
    contenedorEstaciones.agregarEstacion(estacion4)

    iterador = iter(contenedorEstaciones.getEstaciones())

    #Para borrar el siguiente elemento, elimino el primer elemento
    x =  next(iterador)
    del x

    #Recorro la coleccion de objetos, ya no estará el primer elemento
    for estacion in contenedorEstaciones.getEstaciones():
        time.sleep(1)
        print(next(iterador))

    #Esto no va a funcionar :C
    #for estacion in contenedorEstaciones:
        #print(estacion.getFrecuencia())
