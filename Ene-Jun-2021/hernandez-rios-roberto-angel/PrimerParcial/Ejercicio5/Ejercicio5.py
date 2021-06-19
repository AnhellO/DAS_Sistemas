import json

from json2html import *

class User(object):

    def __init__(self, name,age,direction):
        self.nombre = name
        self.edad = age
        self.direccion = direction

    def __str__(self):
        return """
            Nombre: {}\nEdad: {}\nDireccion: {}\n
        """.format(self.nombre, self.edad, self.direccion).strip()


    def serializar(self, formato='diccionario'):
        form = form.lower()
        if form == 'diccionario':
            return self.__dict__
        elif form == 'json':
            return json.dumps(self.__dict__)
        elif form == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))


usuario = User(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)

print(usuario)
print(usuario.serializar("html"))

