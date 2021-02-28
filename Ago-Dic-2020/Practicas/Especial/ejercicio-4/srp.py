import json
from json2html import * # Instala por medio de pip: https://pypi.org/project/json2html/

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

    def serializar(self, formato='string'):
        formato = formato.lower()
        
        if formato == 'string':
            return str(self)
        
        if formato == 'dict':
            return self.__dict__
        
        if formato == 'json':
            return json.dumps(self.__dict__)
        
        if formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))


user = Usuario(
    nombre='Juanito',
    edad=15,
    direccion='Calle X, #Y Colonia Z'
)

print(user.serializar())