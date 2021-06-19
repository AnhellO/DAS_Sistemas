import json
# Descarga esta librería con el comando 'pip install json2html'
#descarga libreria con el comando pip install json2xml
from json2html import *
#importa librerias para hacer el formato xml
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

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


    # defnir el single of responsability: cada función solo debe tenerr una funcionalidad
    # se declara cada funcion formato_"tipo" para definirl el tipo de documento
    # cada función  recibe un formato y  se define el tipo  y retorna  la representación de cada uno
    def formato_string(self, formato='string'):
        return str(self)

    def formato_diccionario(self, formato="diccionario"):
        return self.__dict__
    
    def formato_json(self, formato="json"):
        return json.dumps(self.__dict__)
    
    def formato_html(self, formato="html"):
        return json2html.convert(self.formato_json())

    def formato_xml(self, formato="xml"):
        data = readfromstring(self.formato_json()) # obtener el xml de una cadena json
        return ''.join(json2xml.Json2xml(data).to_xml().split()) #retorna el xml

user = Usuario(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)

print(user.formato_xml())# imprime el xml



#¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
"""
    primero tendriamos que descargar primero la libreria json2xml para generar el xml:desúes se 
    importa, luego obtiene el xml de una cadena json y después retorna el xmml, en el caso del yaml también se tendria que buscar
    la librería que se usa para coonvertirlo en formato yaml y luego declarar un metodo con su respectiva operación para llegar a ese formato.
 
"""
#¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
"""
    identificar que patron se le acomodadaría mejor para hacerlo más sencillo, porque si seguimos agregando muchas instancias serían demasiadas y sería
    poco entendible
"""