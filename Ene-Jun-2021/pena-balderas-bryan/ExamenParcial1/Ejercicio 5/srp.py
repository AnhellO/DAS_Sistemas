import json
# Descarga esta librería con el comando 'pip install json2html'
from json2html import *

class Usuario(object):
    #si ya tenemos definidos nuestros atributos no es necesario pedir con **args
    def __init__(self, nombre,edad,direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    #Quite los getters y setters ya que no tenian caso de ser porque desde la misma instancia del objeto se pueden llamar a los
    #atributos o asignarles valores

    def __str__(self):
        return """
            Nombre: {}\nEdad: {}\nDireccion: {}\n
        """.format(self.nombre, self.edad, self.direccion).strip()

    
    def serializar(self, formato='diccionario'):
        formato = formato.lower()
        #Quite el formato de string ya que la misma funcion de str nos devulve ese formato
        if formato == 'diccionario':
            return self.__dict__
        elif formato == 'json':
            return json.dumps(self.__dict__)
        elif formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))

    


user = Usuario(
    nombre='Ramanujan',
    edad=25,
    direccion='Calle X, #Y Colonia Z'
)

print(user)
print(user.serializar("html"))


#¿Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
#Solo se agregaria un if que evalue, si entra en ese if, lo ideal seria crear una funcion que haga todo el proceso
#de esta forma tendriamos la funcion que evalua a que tipo de formato se quiere pasar y una funcion
#que pase a xml o yalm

#¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
#EN ese caso lo ideal seria sacar las funciones del objeto usuario y crear una clase especifica
#para realizar la serializacion, que no dependa del usuario si no que se llame cuando sea