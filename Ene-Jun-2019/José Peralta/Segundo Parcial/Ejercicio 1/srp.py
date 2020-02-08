import json
from json2html import *

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

# Se elimina el método serializar de la clase Usuario
# En su lugar, se crea una clase Serializador
# Los métodos de Serializador son estáticos, por lo que no es necesario instanciarlo

class Serializador():
    # Cada formato tiene un método propio de serialización
    # Es posible agregar otros formatos de serialización como métodos estáticos de la clase serializador
    # Además, la clase Serializador permite serializar cualquier objeto, no necesariamente uno de la clase Usuario
    @staticmethod
    def serializar(objetivo, formato='string'):
        # El método serializar contiene un diccionario cuyas llaves son los formatos
        # A cada llave le corresponde el método estático que sirve para serializar un objeto con ese formato
        index = {'string':Serializador.serial_as_string(objetivo),
        'diccionario':Serializador.serial_as_dictionary(objetivo),
        'json':Serializador.serial_as_json(objetivo),
        'html':Serializador.serial_as_html(objetivo)}
        # Se devuelve únicamente el valor que corresponde al formato solicitado
        return index[formato.lower()]

    @staticmethod
    def serial_as_string(objetivo):
        return str(objetivo)

    @staticmethod
    def serial_as_dictionary(objetivo):
        return objetivo.__dict__

    @staticmethod
    def serial_as_json(objetivo):
        return json.dumps(objetivo.__dict__)

    @staticmethod
    def serial_as_html(objetivo):
        return json2html.convert(json=json.dumps(objetivo.__dict__), )

if __name__ == '__main__':
    usr = Usuario(
        nombre='Juanito',
        edad=15,
        direccion='Calle X, #Y Colonia Z'
        )
    print(Serializador.serializar(usr))
