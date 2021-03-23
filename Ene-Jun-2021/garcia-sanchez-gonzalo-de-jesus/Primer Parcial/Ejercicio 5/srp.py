#Goncho
import json

# Descarga esta librería con el comando 'pip install json2html'
from json2html import *


class Usuario(object):
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

    def serializarString(self):
        return str(self)

    def serializarDiccionario(self):
        return self.__dict__

    def serializarJSON(self):
        return json.dumps(self.__dict__)

    def serializarHTML(self):
        return json2html.convert(json=json.dumps(self.__dict__))


user = Usuario(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)


print(user.serializarJSON())