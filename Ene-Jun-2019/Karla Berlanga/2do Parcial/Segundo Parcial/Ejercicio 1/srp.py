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

"""
Aplicando el principio de Single Responsability Principle
"Una clase debe tener una sola razón para existir"
En otras palabras, nuestras clases y los objetos que creamos
debe tener una sola razón, se podría entender algo como
no podemos "amontonar", por decirlo de alguna manera, toda nuestra lógica
en el main, por dar un ejemplo.

Justa ésta situación la estamos viendo en el código original
de esta ejercicio, en donde tenemos la clase Usuario y
esta a su vez tiene un método llamado serialización.
Cabe mencionar que el código funciona bien, mas sin embargo se
está violando el principio Single Responsability Principle,
ésta violación ocurre dentro del método serialización pues está
en la misma clase que Usuario, aunque este método está relacionado,
el método de serialización forma parte de  la lógica del programa
no del comportamiento que pudiese llegar a tener el Usuario.
Es por ello que debemos de separar este método de la siguiente manera
"""
class Serializar():

        def __init__(self, usr):
            self.usr = usr

        def String(self):
            return str(self.usr)

        def Diccionario(self):
            return self.usr.__dict__

        def Json(self):
            return json.dumps(self.usr.__dict__)

        def Html(self):
            return json2html.convert(json=json.dumps(self.usr.__dict__), )

def main():
    usr = Usuario(
        nombre='Juanito',
        edad=15,
        direccion='Calle X, #Y Colonia Z'
    )
    usuario =Serializar(usr)

    print(usuario.String())
    print(usuario.Diccionario())
    print(usuario.Json())
    print(usuario.Html
    ())


"""
PREGUNTAS:
1. ¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
    Una vez realizados los cambios, vemos que para ésta pregunta es más sencillo
    agregar una nueva función más como XML o YAML y solo estamos agregando más funcionalidades
    a la nuestra clase Serialización no modificandola.

2.¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
    Para este caso, pienso que vendría bien aplicar el principio de Open/Closed Principle
    en donde se agregaría una interfaz de serialización para cualquier objeto
    serializable.
    Así todos los objetos compartirían los métodos de dicha interfaz.

"""

if __name__ == '__main__':
    main()
