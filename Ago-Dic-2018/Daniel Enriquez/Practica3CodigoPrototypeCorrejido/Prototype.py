from copy import deepcopy

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, editorial, obj):
        #Almacena un objeto para que pueda ser clonado mas tarde
        self._objects[editorial] = obj

    def unregister_object(self, editorial):
        #Elimina un objeto de los que se tiene almacenados
        del self._objects[editorial]

    def clone(self, editorial, **attr):
        #clona u objeto almacenado y agrega o remplaza atributos
        obj = deepcopy(self._objects[editorial])
        obj.__dict__.update(attr)
        return obj

class Libro:
    libro_editorial = None

prototype=Prototype()
libro = Libro()
libro.libro_editorial = "Santillana"

print('Editorial: '+libro.libro_editorial)
prototype.register_object('Santillana', libro)

libro2 = prototype.clone('Santillana', libro_editorial='De Mexico')
print('Editorial: '+libro2.libro_editorial)


libro3= prototype.clone('Santillana', libro_editorial='Internacional')
print('Editorial: '+libro3.libro_editorial)
