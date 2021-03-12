"""
    'A module, a class or a function has to only do one thing. In other words, they have to have only one responsibility.'
    Con esta premisa sacada del link adjunto, rápidamente lo que se me vino a la mente fue desglosar la función serializar,
    ya que esta misma función se encarga de convertir un objeto en JSON, HTML, String y a un diccionario. Tiene la responsabilidad
    de hacer 4 acciones. Aparte, está dentro de la clase usuario. Esto hizo que se me viniera a la mente el anti-patrón llamado 
    'Objeto todopoderoso', ya que tiene una funcionalidad que, aparte de que no tiene mucho que ver con un usuario, 
    aún así con esa función tiene el 'poder' de serializar objetos de diferentes maneras. 
    
    Lo que hice fue sacar esa 'funcionalidad' en una clase y, dentro de la misma, crear 4 métodos los 
    cuales se encargarán de convertir un objeto en JSON, HTML, etc. 
    
    Esto hace que el código sea reutilizable, ya que si quiero serializar un objeto de tipo Alumno, sólo instancio la clase 
    serializar, le paso como argumento mi objeto y mando a llamar el método deseado. Así no tengo que escribir varias veces la 
    función serializar dentro de cada clase que escriba y así 'le doy esa funcionalidad' a todos los objetos para que la clase 
    Usuario no sea la única capaz de serializarse.

    ------------

    -¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
    
    Primero que nada se agregan los test. Una vez que se agregan, ahora sí se escribe el código necesario para que los tests pasen
    correctamente.
    En caso de que se pueda refactorizar, se refactoriza y se agregan nuevos tests. Estos tests tienen que pasar también.
    Lo agregaría en la clase Serialización como método, y esta clase tal vez lo ponga en un archivo separado llamado modulos o 
    parecido para poder tener la funcionalidad en todo mi programa.

    -¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
    
    Creo que respondí la pregunta antes de leerla. xD
    
    La mejor manera es extraer la funcionalidad en una clase capaz de serializar objetos.
"""
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

class Serializar:
    def __init__(self, usuario: Usuario):
        self._usuario = usuario

    def to_str(self):
        return str(self._usuario)

    def to_json(self):
        return json.dumps(self._usuario.__dict__)

    def to_html(self):
        pass

    def to_dict(self):
        pass

user = Usuario(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)

print(Serializar(user).to_json())