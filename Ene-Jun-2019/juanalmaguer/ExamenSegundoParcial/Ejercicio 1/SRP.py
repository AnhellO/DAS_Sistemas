import json
from json2html import *

#De acuerdo al Single Responsibility Principle las clases deben de tener una sola responsabilidad sobre una parte
# de la funcionalidad del software

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

#Se define la clase usuario con sus respectivos argumento y metodos set & get
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

# ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
#  Hay diferentes modulos que ofrece python para la serializacion de archivos como el xml2json(en el caso de XML)
#  y el Yaml(en caso de Yaml) con los cuales agregaríamos otro elif en nuestro def serializar
#  para serializar este tipo de formatos

# ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
#   Se utilizaria la misma clase Serializador para dar soporte a otros objetos ademas de los instanciados por la clase Usuario