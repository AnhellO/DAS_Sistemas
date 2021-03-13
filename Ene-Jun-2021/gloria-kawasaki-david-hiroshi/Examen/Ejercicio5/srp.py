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


    def serializar(self, formato='string'):
        formato = formato.lower()
        
        if formato == 'string':
            return str(self)
        elif formato == 'diccionario':
            return self.__dict__
        elif formato == 'json':
            return json.dumps(self.__dict__)
        elif formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))

    def serializarString(self):
        return str(self)

    def serializarDict(self):
        return self.__dict__

    def serializarJson(self):
        return json.dumps(self.__dict__)

    def serializarHtml(self):
        return json2html.convert(json=json.dumps(self.__dict__))

if __name__=='main':
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )

    print(user.serializarHtml())