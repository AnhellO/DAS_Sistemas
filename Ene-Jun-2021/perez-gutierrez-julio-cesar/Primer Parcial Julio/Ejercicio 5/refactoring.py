import json

from json2html import *

class Usuario(object):

    #quiete los **args porque que ya estaban bien definidos los atributos que tendria esta clase
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    
    #tambien omite las otras funciones de set y get porque creo que son redundantes
    def __str__(self):
        return """
            Nombre: {}\nEdad: {}\nDireccion: {}\n
        """.format(self.nombre, self.edad, self.direccion).strip()
    #aqui aplico el single responsibility ya que la funcion anterior 
    # serializaba todos los formatos
    #lo que hice fue hacer una para cada caso
    def serializar_string(self):
        return str(self)
    
    def serializar_diccionario(self):
        return self.__dict__
    
    def serializar_json(self):
        return json.dumps(self.__dict__)
    
    def serializar_html(self):
        return json2html.convert(json=json.dumps(self.__dict__))

#¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
#Tendria que agregar nuevas funciones para esos formatos 
#tal vez agregar mas librerias 
#ya que su sintaxis combina conceptos de varios lenguajes HTML, C, Perl y Python.
#y se volveria mas complejo, tambien se podria usar algun patron de diseño creo
#como el facade ya que pudieramos ocultar la complejidad de cada formato

#¿Qué sucedería si quiero soporte para serialización a
# otros objetos aparte de los instanciados por la clase Usuario?
#la instancia de esos objetos tendria que heredar las funciones de la clase Usuario
if __name__ == '__main__' :
    user = Usuario('Ramanujan',25,'Calle X, #Y Colonia Z'
    )

    print(user.serializar_json())