import json
from abc import ABC, abstractmethod
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

    #Reemplaze la funcion serializar por 4 funciones por separado, ya que segun el srp cada funcion tiene que solo hacer una cosa,
    #en base a eso entiendo que ahora lo hace, basicamente si a la funcion que entro no le pertenece ese formato se lo pasa al siguiente
    #y cada una solo realiza su tarea de regresar los datos con el formato adecuado  
    def serializar(self, formato):
        formato = formato.lower()
        if formato == "string":
            return str(self)
        else: 
            return self.serializarDic(formato)
    
    def serializarDic(self, formato):
        if formato == "diccionario":
            return self.__dict__
        else: 
            return self.serializarJson(formato)

    def serializarJson(self, formato):
        if formato == "json":
            return json.dumps(self.__dict__)
        else:
            return self.serializarHtml(formato)

    def serializarHtml(self, formato):
        if formato == "html":
            return json2html.convert(json=json.dumps(self.__dict__))

    #si quisieras agregar otro formato de serializacion en este caso no habria problema solo se agrega su funcion, se le da su logica y se le llama por la funcion html con un else: return funcion
    #tampoco creo que hubiera algun problema con otros objetos al implementarlo asi, mientras tengan un str 
user = Usuario(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)

print(user.serializar("html"))