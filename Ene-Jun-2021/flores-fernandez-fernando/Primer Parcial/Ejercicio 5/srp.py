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
#visto en el ejemplo de single responsibility principle el cual dice que hay que crear una funcion que solo se responsabilice de una sola accion. 
#separe la funcion serializar debido a que era compleja y por lo tanto a la hora de debbuguear seria mas tardado encontrar un error dentro de su 
#construccion ya que era un flujo de muchas desiciones que se puede simplificar destruyendola en funciones singulares que tomen el flujo de 
#las decisiones  
    def serializar_string(self):
        return str(self)
    
    def serializar_dict(self):
        return self.__dict__
    
    def serializar_json(self):
        return json.dumps(self.__dict__)
    
    def serializar_html(self):
        return json2html.convert(json=json.dumps(self.__dict__))
    
    def serializar(self, formato):
        formato = formato.lower()
        
        if formato == 'string':
            return str(self)
        elif formato == 'diccionario':
            return self.__dict__
        elif formato == 'json':
            return json.dumps(self.__dict__)
        elif formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))

def main():
    

    user = Usuario(
        nombre='Ramanujan',
        edad=25,
        direccion='Calle X, #Y Colonia Z'
    )
    serializar = user.serializar_html()
    
    print(serializar)
    print(user.serializar("string"))
    print(user.serializar("diccionario"))
    print(user.serializar("json"))
    print(user.serializar("html"))

if __name__ == '__main__':
    main()        
    
# Qué sucedería si quiero agregar otro formato de serialización más complejo como XML o Yaml?
# primero seria buscar alguna libreria que se encargue de eso como lo utilizado en json2html 
# para la serializacion como pyxser para XML o yamlize para YAML y se crea una nueva funcion 
# que utilice esas librerias para la serializacion compleja y mandarla a llamar como las anteriores.

# ¿Qué sucedería si quiero soporte para serialización a otros objetos aparte de los instanciados por la clase Usuario?
# una seria modificar las funciones para que en lugar de usar self, utilucen un objeto como parametro y regrese la serializacion
# y otra seria sacar esas funciones de la clase Usuario y crear una clase exclusiva para serializar cualquier tipo de objetos
#que tenga como atributo el objeto que recibe para la serializacion.    