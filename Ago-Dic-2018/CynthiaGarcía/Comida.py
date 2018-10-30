from abc import ABCMeta, abstractmethod

 def Comida(object):
 	def __init__(self, pan, Carne,Verduras, aderezos, Combo)
        self.pan=pan
        self.Carne=carne
        self.Verduras=Verduras
        self.aderezos=aderezos
        self.Combo=combo

        def __str__(self):
        return ('Hamburguesa: \nde pan: {} \ncon Carne: {} \nCon : {} \n En:{}'.format(self.pan, self.Carne, self.Verduras, self.aderezos, self.Combo))
	
		#def __str__(self):
        #return ('Hot dog: \nde pan: {} \ncon Carne: {} \nCon : {} \n En:{}'.format(self.pan, self.Carne, self.Verduras, self.aderezos, self.Combo))
	
class Builder:  
	__metaclass__ = ABCMeta  

	def set_pan(self, value):
		pass

	def set_carne(self, value):
		pass

	def set_verduras(self, value):
		pass

	def set_aderezos(self, value):
		pass

	def set_aderezos(self, value):
		pass

	def set_combo(self, value):
		pass	

	def get_result(self):
		pass

class ComidaBuilder(Builder):
	def __init__(self):
		self.comida=Comida()

	def set_pan(self, value):
		self.comida.pan=value

	def set_carne(self, value):
		self.comida.carne=value

	def set_verduras(self, value):
		self.comida.Verduras=value

    def set_aderezos(self, value):
		self.comida.aderezos=value

	def set_combo(self, value):
		self.comida.combo=value

	def get_result(self):
		return self.pizza	


class Director(object): #se encarga de recibir para hacer la construcción
	def construct():
		builder=ComidaBuilder()
		builder.set_pan('bimbollo') 
		builder.set_carne('casera')
		builder.set_verduras('Tomate, Cebolla')
		builder.set_aderezos('mayonessa')
		builder.set_combo('2 Hamburguesas')
		return builder.get_result()

#Me falto para el hotdog por tiempo :'(
comida=Director.construct()
print (comida)		