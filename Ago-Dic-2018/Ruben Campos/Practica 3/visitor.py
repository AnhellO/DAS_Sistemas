import abc

#Visitante, clase abstracta con funcion visitar
class VisitanteCarritoCompras(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visitar(self, item):
        pass

#Element, clase abstracta con funcion accept
class ItemElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self):
        pass

#Estructuras de objetos: Libro, fruta
#Elemento concreto
class Libro(ItemElement):
    def __init__(self, costo, codigo):
        self.precio = costo
        self.codigo = codigo

    def get_precio(self):
        return self.precio

    def get_codigo(self):
        return self.codigo

    def accept(self, visitor):
        return visitor.visitar(self)

#Elemento concreto
class Fruta(ItemElement):
    def __init__(self, precio, peso, nombre):
        self.precio = precio
        self.peso = peso
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def get_peso(self):
        return self.peso

    def get_nombre(self):
        return self.nombre

    def accept(self, visitor):
        return visitor.visitar(self)

#Visitante Concreto,  implementa la interfaz de Visitor, y añade la funcionalidad nueva a implementar
class VisitanteCarritoComprasImpl(VisitanteCarritoCompras):
    def visitar(self, item):
        if isinstance(item, Libro):
            costo = 0
            #aplicar un descuento de 5 pesitos si el precio es mayor a 50
            if item.get_precio() > 50:
                costo = item.get_precio() - 5
            else:
                costo = item.get_precio()
            print("Codigo de libro:: {} costo = {}".format(item.get_codigo(), costo))
            return costo
        elif isinstance(item, Fruta):
            #calcular el costo en base al precio y peso del producto
            costo = item.get_precio() * item.get_peso()
            print("Costo de {} = {}".format(item.get_nombre(), costo))
            return costo

# Recorremos una lista de objetos a visitar y calculamos el costo total
def calcular_precio(items):
    visitor = VisitanteCarritoComprasImpl()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum

if __name__ == '__main__':
    items = [
        Libro(20, "1234"),
        Libro(100, "5678"),
        Fruta(10, 2, "Mango"),
        Fruta(5, 5, "Naranja")
    ]

    total = calcular_precio(items)
    print("Costo total = {}".format(total))
