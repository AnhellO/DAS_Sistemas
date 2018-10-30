class EstacionDeRadio:
    _frecuencia = None

    def __init__(self, frecuencia):
        self._frecuencia = frecuencia

    def getFrecuencia(self):
        return self._frecuencia
##################################3#################################################################################
class Estaciones:
    _estaciones = []

    def agregarEstacion(self, estacion):
        self._estaciones.append(estacion)

    def getEstaciones(self):
        return [estacion.getFrecuencia() for estacion in self._estaciones]

    def _init_(self, n):
        self.i = 0
        self.n = n

    def _iter_(self): #método es lo que hace iterable un objeto.
        return self #El valor de retorno de __iter__ es un iterator

    def next(self): #Cada vez que llamo al metodo next en el iterador nos da el siguiente elemento.
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration() #Si no hay más elementos, se genera una StopIteration .
##############3################################################################################################
if __name__ == '__main__': # esta logica final es el pasar nuestra lista de "estaciones" para que pueda ser iterablre
    contenedorestaciones = ['89.9', '101.2', '101.3', '100.4'] #estaciones se guardan en una lista como str
    iterator = iter(contenedorestaciones) #(tmb se puede recorrer la lista con un for i in estaciones y pasar cada objeto float a str)
    next(iterator) #y guardarla a en una nueva lista, pero seria inecesario | recorrer la pocicion desead con un next()
    contenedorestaciones.pop(0) #y con pop retirar el objeto de esta lista
    print(contenedorestaciones) #ya solo la im´primo para vereificar
