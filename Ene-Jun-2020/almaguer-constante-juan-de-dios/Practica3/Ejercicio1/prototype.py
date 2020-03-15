import copy


# se crea la clase OvejaPrototype para clonar a la clase Oveja
class OvejaPrototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attr)
        return obj


# Se crea la clase oveja
class Oveja(object):

    def __init__(self, nombre, tipo, sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.sonido = sonido

    def set_nombre(self, nombre):
        self.nombre

    def get_nombre(self):
        return self.nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo

    def set_sonido(self, sonido):
        self.sonido = sonido

    def get_sonido(self):
        return self.sonido

    # devuelve la representación en string del objeto
    def __str__(self):
        return f'Nombre: {self.nombre}\nTipo: {self.tipo}\n' \
               f'Sonido: {self.sonido}'


prototype = OvejaPrototype()
# Se crea una instancia de la Oveja que será clonada
oveja1 = Oveja("Ovejuan", "Dorada", "bee")

#se registra la oveja en la clase prototype
prototype.register_object('Ovejuan', oveja1)
#se clona una oveja con la oveja ya existente en la clase
oveja2 = prototype.clone('Ovejuan', nombre='George')

print(oveja1)
print(oveja2)
