from typing import List


class Restaurante:
    def __init__(self, restaurante_name , cuisine_type):
       self.restaurante_name= restaurante_name
       self.cuisine_type=cuisine_type
    def Describe_restaurante(self):
       print("nombre: ",self.restaurante_name.title() +", tipo: "+ self.cuisine_type)
    def open_restaurante(self):
     print(self.restaurante_name.title() +" esta abierto")

class IceCreamStand(Restaurante):
    def __init__(self, restaurante_name, cuisine_type):
        super().__init__(restaurante_name, cuisine_type)
        self.saboress=['fresa','chocolate','vainilla','pistache','arandanos']
    def sabores (self):
        print(list(self.saboress))

helado =IceCreamStand('chico timido','heladeria')
helado.Describe_restaurante()
helado.sabores()