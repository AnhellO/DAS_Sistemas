import copy
class Oveja:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo

    def get_tipo(self):
        return self.tipo

class SelfReferencingEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

class SomeComponent:
        def __init__(self, nombre, tipo, some_circular_ref):
            self.nombre = nombre
            self.tipo = tipo
            self.some_circular_ref=some_circular_ref
        def __copy__(self):
            nombre= copy.copy(self.nombre) 
            tipo=copy.copy(self.tipo)
            some_circular_ref = copy.copy(self.some_circular_ref)
            new = self.__class__(nombre,tipo, some_circular_ref)
            new.__dict__.update(self.__dict__)

            return new
        def __deepcopy__(self, memo=None):
            if memo is None:
                memo = {}
            nombre= copy.copy(self.nombre) 
            tipo=copy.copy(self.tipo)
            some_circular_ref = copy.copy(self.some_circular_ref)
            new = self.__class__(nombre,tipo, some_circular_ref)
            new.__dict__.update(self.__dict__)
            return new
if __name__ == "__main__":
    OVEJA=Oveja("Dolly","1")
    circular_ref=SelfReferencingEntity()
    clon=SomeComponent(OVEJA.get_nombre,OVEJA.get_tipo,circular_ref)
    shallow_copied_component=copy.copy(clon)


        