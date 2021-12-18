class Restaurante:
    def __init__(self, restaurante_name , cuisine_type) :
       self.restaurante_name= restaurante_name
       self.cuisine_type=cuisine_type
       self.number_served= 0 
    def Describe_restaurante(self):
       print("nombre: ",self.restaurante_name.title() +", tipo: "+ self.cuisine_type + "clientes atendidos: " + str(self.number_served) )
    def open_restaurante(self):
       print(self.restaurante_name.title() +" esta abierto")
    def set_number_served(self,number_served):
        self.number_served=number_served
    def increment_number_served (self, incremento) :
        self.number_served += incremento


restaurante = Restaurante('pizza hot', 'fast food')
print(restaurante.restaurante_name.title())
restaurante.number_served=23
print(restaurante.cuisine_type)
restaurante.Describe_restaurante()
restaurante.open_restaurante()
restaurante.set_number_served(5)
restaurante.increment_number_served(5)
restaurante.Describe_restaurante()
