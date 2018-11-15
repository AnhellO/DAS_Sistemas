from __future__ import print_function
from abc import ABCMeta, abstractmethod
class ComidaRapida(object):
	def __init__(self, panham='', panhot='', carneham='', carnehot='', verdurasham='', verdurashot='', condimentosham='', condimentoshot='', comboham='', combohot=''):
         self.panham=panham
         self.panhot=panhot
         self.carneham=carneham
         self.carnehot=carnehot
         self.verdurasham=verdurasham
         self.verdurashot=verdurashot
         self.condimentosham=condimentosham
         self.condimentoshot=condimentoshot
         self.comboham=comboham
         self.combohot=combohot
         def __str__(self):
             return ('La orden contiene: \npan hamburguesa: {} \npan hotdog: {} \ncarne hamburguesa: {} \ncarne hotdog: {} \ncon verduras hamburguesa: {} \nverduras hot dog: {} \ncondimentos hamburguesa: {} \ncondimentos hotdog: {} \ncombo hamburguesa: {} \ncombo hot dog: {}'.format(self.panham, self.panhot, self.carneham, self.carnehot, self.verdurasham, self.verdurashot, self.condimentoshot, self.comboham, self.combohot))

class Builder:
    __metaclass__ = ABCMeta  #Especifique una clase abstracta para crear partes de un Producto objeto
    def set_panham(self, value):
        pass
    def set_panhot(self, value):
        pass
    def set_carneham(self, value):
        pass
    def set_carnehot(self, value):
        pass
    def set_verdurasham(self, value):
        pass
    def set_verdurashot(self, value):
        pass
    def set_condimentosham(self, value):
        pass
    def set_condimentoshot(self, value):
        pass
    def set_comboham(self, value):
        pass
    def set_combohot(self, value):
        pass
    def get_result(self):
        pass

class ComidaRapidaBuilder(Builder):
    def __init__(self):
        self.comidarapida=ComidaRapida()
    def set_panham(self, value):
        self.comidarapida.panham=value
    def set_panhot(self, value):
        self.comidarapida.panhot=value
    def set_carneham(self, value):
        self.comidarapida.carneham=value
    def set_carnehot(self, value):
        self.comidarapida.carnehot=value
    def set_verdurasham(self, value):
        self.comidarapida.verdurasham=value
    def set_verdurashot(self, value):
        self.comidarapida.verdurashot=value
    def set_condimentosham(self, value):
        self.comidarapida.condimentosham=value
    def set_condimentoshot(self, value):
        self.comidarapida.condimentoshot=value
    def set_comboham(self, value):
        self.comidarapida.comboham=value
    def set_combohot(self, value):
        self.comidarapida.combohot=value
    def get_result(self):
        return self.comidarapida

class Director(object): #se encarga de recibir para hacer la construcción
	def construct():
         builder=ComidaRapidaBuilder()
         builder.set_panham('mediano') 
         builder.set_carneham('res')
         builder.set_verdurasham('lechuga, tomate, sin cebolla, pepinillos') 
         builder.set_condimentosham('catsup, mostaza, sin mayonesa')
         builder.set_comboham('en combo con papas y refresco')
         builder.set_panhot('chico') 
         builder.set_carnehot('pavo')
         builder.set_verdurashot('tomate, cebolla, jalapeños') 
         builder.set_condimentoshot('catsup, mostaza, sin mayonesa')
         builder.set_combohot('en combo con papas y refresco')
         return builder.get_result()
comidarapida=Director.construct()
print (comidarapida)