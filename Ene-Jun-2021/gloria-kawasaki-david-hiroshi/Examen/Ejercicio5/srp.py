import json
# Descarga esta librería con el comando 'pip install json2html'
from json2html import *

class Usuario(object):
    '''
    Esta función inicializa la clase cuando se instancia
    '''
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.edad = args.get('edad')
        self.direccion = args.get('direccion')

    '''
    Grupo de getters y setters para obtener y asignar los valores de las variables
    desde fuera de la clase
    '''
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

    '''
    Esta función vuelve al objeto a un string
    '''
    def __str__(self):
        return """
            Nombre: {}\nEdad: {}\nDireccion: {}\n
        """.format(self.nombre, self.edad, self.direccion).strip()

    '''
    Para este ejercicio lo que se hace es dividir esta función en funciones más pequeñas,
    de una sola funcionalidad
    '''
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
    
    '''
    Esta función regresa el objeto transformado en un string
    '''
    def serializarString(self):
        return str(self)

    '''
    Esta función regresa el objeto transformado en un diccionario
    '''
    def serializarDict(self):
        return self.__dict__

    '''
    Esta función regresa el objeto transformado en un Json
    '''
    def serializarJson(self):
        return json.dumps(self.__dict__)

    '''
    Esta función regresa el objeto transformado en un html
    '''
    def serializarHtml(self):
        return json2html.convert(json=json.dumps(self.__dict__))

if __name__=='main':
    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )

    print(user.serializarHtml())