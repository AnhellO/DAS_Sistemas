
class Restourant():
    def __init__(self,restourant_name,cuisine_type):
        self.restourant_name = restourant_name
        self.cuisine_type = cuisine_type
        #? atributo del ejercicio 9.4 
        self.number_serverd = 0

    def describe_restourant(self):
        descripcion =f'{self.restourant_name}, {self.cuisine_type}'
        return descripcion.title()

    def open_restourant(self):
        return (f'Restourant {self.restourant_name.title()} is open ')
    
    #?add a method of exercise 9.4
    def set_number_served(self,number_serverd):
        self.number_serverd = number_serverd
        return self.number_serverd
    
    #? metodo que incrementa el numero de clientes atendidos
    def increment_number_serverd(self, increment):
        self.number_serverd += increment    
        return self.number_serverd