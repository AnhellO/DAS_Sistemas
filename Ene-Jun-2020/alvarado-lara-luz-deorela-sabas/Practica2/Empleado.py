#IMPORTAMOS CLASE PERSONA
from Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, peso, estatura, pasatiempo, id, puesto):
      #HEREDAMOS LOS ATRIBUTOS DE LA CLASE PERSONA
      super().__init__(nombre, edad, peso, estatura, pasatiempo)
      #AGREGAMOS LOS ATRIBUTOS QUE PERTENECEN A UN EMPLEADO
      self.id = id
      self.puesto = puesto 
      #GET Y SETT PARA ATRIBUTOS DE EMPLEADO
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_puesto(self):
        return self.puesto
    def set_puesto(self, puesto):
        self.puesto = puesto
    def __str__(self):
        registro = {'Nombre': {self.nombre}, 'Edad': {self.edad}, 'Peso': {self.peso}, 'Estatura': {self.estatura}, 'Pasatiempo': {self.pasatiempo}, 'ID': {self.id}, 'Puesto': {self.puesto}}
        #return f'Nombre: {self.nombre}\nEdad: {self.edad}\n años\nPeso: {self.peso} kg \nEstatura: {self.estatura} cm \nPasatiempo: {self.pasatiempo} \nID: {self.id} \nPuesto: {self.puesto} '
        return registro

"""
empleado = Empleado(nombre='Jose', edad='39', peso='85', estatura='1.85', pasatiempo='Leer, Cantar', id= '445522', puesto ='Gerente')
print(empleado)
"""
