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


class Serializador(object):
    def __init__(self, obj: Usuario):
        self._obj = obj
    
    # TODO: Refactorizar esto a utilizar el patrón 'Strategy'
    # y la técnica https://refactoring.guru/replace-conditional-with-polymorphism
    def serializar(self, formato='string'):
        formato = formato.lower()
        
        if formato == 'string':
            return self._serializar_string()
        elif formato == 'diccionario':
            return self._serializar_dict()
        elif formato == 'json':
            return self._serializar_json()
        elif formato == 'html':
            return self._serializar_html()
    
    def _serializar_string(self):
        return str(self._obj)
    
    def _serializar_dict(self):
        return self._obj.__dict__

    def _serializar_json(self):
        return json.dumps(self._obj.__dict__)

    def _serializar_html(self):
        return json2html.convert(json=json.dumps(self._obj.__dict__))
