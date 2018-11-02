
class Estaciones:
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
estaciones = ['89.9', '101.2', '101.3', '100.4']
iterador = iter(estaciones)

#Imprime la lista inicial
print(estaciones)
#mientras la lista no esta vacia, recorre la lista para eliminar el elemento cero, siempre es el elemento 0 porque cada que hace una eliminacion, la lista cambia de tamaño

while estaciones != []:
 	for x in estaciones:
	  
	   estaciones.pop(0)
	   print(estaciones)

       #estaciones.pop(1)  estas impresiones son por si quiero eliminar otro elemento en diferente orden.
       #print(estaciones)

       #estaciones.pop(2)
       #print(estaciones)
estaciones == ['']










