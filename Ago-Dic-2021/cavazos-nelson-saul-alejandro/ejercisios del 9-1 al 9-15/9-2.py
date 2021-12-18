class Restaurante:
    def __init__(self, restaurante_name , cuisine_type):
       self.restaurante_name= restaurante_name
       self.cuisine_type=cuisine_type
    def Describe_restaurante(self):
       print("nombre: ",self.restaurante_name.title() +", tipo: "+ self.cuisine_type)
    def open_restaurante(self):
     print(self.restaurante_name.title() +" esta abierto")


restaurante_1=Restaurante('viena', 'cafeteria')
restaurante_1.Describe_restaurante()

restaurante_2=Restaurante('MCdonals','Fast food')
restaurante_2.Describe_restaurante()

restaurante_3=Restaurante('el monster','bar')
restaurante_3.Describe_restaurante()