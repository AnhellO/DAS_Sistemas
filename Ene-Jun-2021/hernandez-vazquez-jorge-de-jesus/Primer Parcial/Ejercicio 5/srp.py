import json
# Descarga esta librería con el comando 'pip install json2html'
#from json2html import *
from json2html import *

class Usuario:
    #Se decidio dejar el constructor tal y como estaba
    #Por otra parte, los geters y seters se eliminaron, ya que
    #No hacen falta para estas tareas.
    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.edad = args.get('edad')
        self.direccion = args.get('direccion')


    # Funcion __str__ para la representacion del 
    # Objeto usuario en forma de string
    def __str__(self):
        return f"""Nombre: {self.nombre}\nEdad: {self.edad}\nDireccion: {self.direccion}\n""".strip()

    #Debido al test "test_serializar_str", se noto
    #Que hacía falta una refactorizacion en la
    #Función inicial de serializacion,
    #La funcion "serializar()"
    def serializar_str(self, formato='string'):
        formato = formato.lower()
        if formato == 'string':
            return str(self)


    # Siguiendo el "Single Responsibility Principle"
    # Se decidio dividir la funcion "serializar", en
    # Varias funciones, no solo para refactorizar, sino
    # Para que funcionara
    def serializar_dict(self, formato='diccionario'):
        formato = formato.lower()
        if formato == 'diccionario':
            return self.__dict__
    
    # Como se nota en cada funcion, cada una de ellas
    # Lleva a cabo una serializacion de un objeto
    def serializar_json(self, formato='json'):
        formato = formato.lower()
        if formato == 'json':
            return json.dumps(self.__dict__)

    # En este caso, es un objeto de tipo "Usuario"
    # El cual tiene atributos de nombre, edad y direccion. 
    # Cada funcion debera regresar ese objeto pero en el
    # Formato que le corresponda segun la condicion.
    def serializar_html(self, formato='html'):
        formato = formato.lower()
        if formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))


 #Creamos el objeto e imprimimos para checar su estructura. 
def main():
    user = Usuario(
        nombre="Ramanujan",
        edad=25,
        direccion="Calle X, #Y Colonia Z")
    print(user)
    

if __name__ == "__main__":
    main()