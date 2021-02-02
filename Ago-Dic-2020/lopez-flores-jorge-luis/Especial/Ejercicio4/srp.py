import json
from json2html import * # Instala por medio de pip: https://pypi.org/project/json2html/
from json2xml import json2xml  # Instala por medio de pip: https://pypi.org/project/json2xml/


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

# Hasta aqui los datos son propios de la clase Usuario

# Es importante crear otra clase para que cumpla con las funciones de analisis del formato.
class serializar(Usuario):
    def serialize(self, formato='string'):#aqui de igual manera podemos elegir que formato queremos utilizar.
        formato = formato.lower()

        if formato == 'string':
            return str(self)

        if formato == 'dict':
            return self.__dict__

        if formato == 'json':
            return json.dumps(self.__dict__)

        if formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))
        # Para el xml hay que importar la libreria json2xml y aplicar la configuración segun se explica en la librería.
        if formato == 'XML':
            return json2xml.Json2xml(wrapper="all", pretty=True).to_xml()

    def __str__(self):
        return "Nombre:{}, Edad:{}, direccion:{}".format(self.nombre, self.edad, self.direccion).strip()

user = serializar(
    nombre='juanito',
    edad=15,
    direccion='calle x, #y colonia z')

print(user.serialize())

'''Si quiero soporte para serializar otros objetos aparte de los de usuario,
 tengo que crear otra clase en la que definamos dichos objetos y heredar la clase
 serializar de la nueva clase para que se enfoque el analisis en nuestra nueva clase, y finalmente
 probar con una salida.'''