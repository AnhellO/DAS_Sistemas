class Restaurante:
    def __init__(self, restaurante_name , cuisine_type):
       self.restaurante_name= restaurante_name
       self.cuisine_type=cuisine_type
    def Describe_restaurante(self):
       print("nombre: ",self.restaurante_name.title() +", tipo: "+ self.cuisine_type)
    def open_restaurante(self):
     print(self.restaurante_name.title() +" esta abierto")

restaurante = Restaurante('pizza hot', 'fast food')
print(restaurante.restaurante_name.title())
print(restaurante.cuisine_type)
restaurante.Describe_restaurante()
restaurante.open_restaurante()
