from __future__ import print_function
from abc import ABCMeta, abstractmethod

class Puesto(object):
    def __init__(self, pan='', carne='', verduras='', condimentos='', combo=''):
        self.pan=pan
	self.carne=carne
	self.verduras=verduras
	self.condimentos=condimentos
	self.combo=combo

	
    def __str__(self):
        return ('que va a ordenar: \npan: {} \ncarne: {} \nverduras: {} \ncondimentos: {} \ncombo: {}'.format(self.pan, self.carne, self.verduras, self.condimentos, self.combo))
		
class Builder:  
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_pan(self, value):
        pass
    @abstractmethod
    def set_carne(self, value):
	pass
    @abstractmethod
    def set_verduras(self, value):
	pass
    @abstractmethod
    def set_condimentos(self, value):
	pass
    @abstractmethod
    def set_combo(self, value):
	pass
    @abstractmethod
    def get_result(self):
	pass

    
class puestoBuilder(Builder):
    def __init__(self):
	self.puesto=Puesto()
	
    def set_masa(self, value):
	self.puesto.pan=value
	
    def set_ingre(self, value):
	self.puesto.carne=value
	
    def set_tamaño(self, value):
	self.puesto.verduras=value

    def set_tamaño(self, value):
	self.puesto.condimentos=value

    def set_tamaño(self, value):
	self.puesto.combo=value
	
    def get_result(self):
	return self.puesto
    
class Director(object):
    @staticmethod
    def construct():
	builder=puestoBuilder()
	builder.set_pan('de hoco') 
	builder.set_carne('salchica')
	builder.set_verduras('todas')
	builder.set_condimentos('todos')
	builder.set_combo('en combo')
	return builder.get_result()
    
puesto=Director.construct()
print(puesto)
