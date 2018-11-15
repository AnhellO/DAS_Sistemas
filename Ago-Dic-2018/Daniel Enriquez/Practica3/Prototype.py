from copy import deepcopy

class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        #Almacena un objeto para que pueda ser clonado mas tarde
        self._objects[name] = obj

    def unregister_object(self, name):
        #Elimina un objeto de los que se tiene almacenados
        del self._objects[raza]

    def clone(self, name, **attr):
        #clona u objeto almacenado y agrega o remplaza atributos
        obj = deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj

class Animal:
    animal_name = None

prototype=Prototype()
animal = Animal()
animal.animal_name = "Gato"
print(animal.animal_name)
prototype.register_object('Gato', animal)

perro = prototype.clone('Gato', animal_name='Jeff')
print(perro.animal_name)
