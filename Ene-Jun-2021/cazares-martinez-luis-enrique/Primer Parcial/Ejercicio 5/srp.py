import json
# Se descargo esta librería con el comando 'pip install json2html'
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

# Apartir de aqui se modifico la clase
# Se implemento el patron Single Responsibility Principle el cual consiste en separar una funcion que realiza funciones
# especificas para cada situacion, por consiguiente la funcion "Serealizar" (la cual recibia como parametro el 
# formato con el cual se serealizaba la informacion) dado como resultado 4 metodos encargados de regresar la informacion que se ocupa.
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


# ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
# -R Necesitamos crear un nuevo metodo, que nos serealize la informacion de acuerdo al nuevo Formato que se pide.

# ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
# -R Primero crearimos una clase dedicada a serealizar la informacion de acuerdo al formato que se nos pide,
# dentro de la clase tendriamos metodos especificos para cada formato los cuales reciben como parametro el metodo "__Str__",
# que regresa la informacion ya serealizada acorde a como la necitamos.