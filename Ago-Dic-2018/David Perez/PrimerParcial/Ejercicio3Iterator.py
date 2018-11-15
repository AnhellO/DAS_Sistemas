class EstacionDeRadio:
    _frecuencia = None

    def __init__(self, frecuencia):
        self._frecuencia = frecuencia

    def __iter__(self):
        return self

    def next(self):
        if self._frecuencia < self.n:
            _frecuencia = self._frecuencia
            self._frecuencia += 1
            return _frecuencia
        else:
            raise StopIteration()

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

    myiterator = iter(contenedorEstaciones)
    print(next(myiterator))
    print(next(myiterator))
    print(next(myiterator))
    print(next(myiterator))
print(contenedorEstaciones.getEstaciones())
