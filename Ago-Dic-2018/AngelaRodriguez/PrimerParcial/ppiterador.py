
def getEstaciones(self):
        return [estacion.getFrecuencia() for estacion in self._estaciones]

def init(self, n):
    self.i = 0
    self.n = n

def iter(self): # método que hace iterable un objeto.
    return self #El valor de retorno de _iter_ es un iterator

def next(self): #Cada vez que llamo al metodo next en el iterador nos da el siguiente elemento.
    if self.i < self.n:
        i = self.i
        self.i += 1
        return i
    else:
        raise StopIteration()
             #Si no hay más elementos, se genera una StopIteration.


if __name__ == '__main__': # esta logica final es el pasar nuestra lista de "estaciones" para que pueda ser iterablre
    contenedorEstaciones = ['89.9', '101.2', '101.3', '100.4'] #las estaciones se guardan en una lista como str
    iterator = iter(contenedorEstaciones) #se puede recorrer la lista con un for i in estaciones y pasar cada objeto float a str
    next(iterator)
    #con pop(0)  eliminamos el primer el objeto de esta lista
    contenedorEstaciones.pop(0)
    print(contenedorEstaciones) #yaqui se imprime para ver la lista

