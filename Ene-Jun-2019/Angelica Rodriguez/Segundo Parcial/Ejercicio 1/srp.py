import json
from json2html import *

class Serializador(object):
    def __init__(self, usuario = {}):
        self.usuario = usuario

    def serializar(self, usuario, formato = 'string'):
        formato = formato.lower()

        if formato == 'string':
            return str(self)
        elif formato == 'diccionario':
            return self.__dict__
        elif formato == 'json':
            return json.dumps(self.__dict__)
        elif formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__), )

class Usuario(object):
    """docstring for Usuario"""
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.edad = args.get('edad')
        self.direccion = args.get('direccion')

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_direccion(self):
        return self.direccion

    def __str__(self):
        return """
            Nombre: {}\nEdad: {}\nDireccion: {}\n
        """.format(self.nombre, self.edad, self.direccion).strip()

usr = Usuario(
    nombre='Juanito',
    edad=15,
    direccion='Calle X, #Y Colonia Z'
)

print(Serializador.serializar(usr,'xml'))
# Separé en dos clases elementos distintos
# Cada clase tiene una única responsabilidad
#si agregamos xml se vuelve más complejo
