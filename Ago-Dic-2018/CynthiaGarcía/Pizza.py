from __future__ import print_function
from abc import ABCMeta, abstractmethod

class Pizza(object):
	def __init__(self, masa='', ingre='', tamaño=''):
		self.masa=masa
		self.ingre=ingre
		self.tamaño=tamaño

	def __str__(self):
		return ('Pizza: \nde masa: {} \ncon ingredientes: {} \nde tamaño: {}'.format(self.masa, self.ingre, self.tamaño))
		
class Builder:  
	__metaclass__ = ABCMeta  #Especifique una clase abstracta para crear partes de un Producto objeto

	def set_masa(self, value):
		pass

	def set_ingre(self, value):
		pass

	def set_tamaño(self, value):
		pass

	def get_result(self):
		pass

class PizzaBuilder(Builder):
	def __init__(self):
		self.pizza=Pizza()

	def set_masa(self, value):
		self.pizza.masa=value

	def set_ingre(self, value):
		self.pizza.ingre=value

	def set_tamaño(self, value):
		self.pizza.tamaño=value

	def get_result(self):
		return self.pizza	


class Director(object): #se encarga de recibir para hacer la construcción
	def construct():
		builder=PizzaBuilder()
		builder.set_tamaño('grande') 
		builder.set_ingre('jamon')
		builder.set_masa('delgada')
		return builder.get_result()

pizza=Director.construct()
print (pizza)		