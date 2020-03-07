########################################
##### Decoradores con clases y objetos
########################################

import abc

class SubwayComponent(metaclass=abc.ABCMeta):
	"""docstring for Subway"""
	
	@abc.abstractmethod
	def cost(self):
		pass

	def description(self):
		pass

class SubwayClassicDecorator(SubwayComponent):
	"""docstring for SubwayClassic"""
	
	def cost(self):
		return 40.0

	def description(self):
		return 'Jamón, queso y lechuga'
		
class SubwayChickenConcreteDecorator(SubwayComponent):
	"""docstring for Sub"""
	def __init__(self, sub: SubwayComponent):
		self._sub = sub
	
	def cost(self):
		return self._sub.cost() + 15.0

	def description(self):
		return f'{self._sub.description()}, y pollito empanizado'

class SubwayItalianConcreteDecorator(SubwayComponent):
	"""docstring for Sub"""
	def __init__(self, sub: SubwayComponent):
		self._sub = sub
	
	def cost(self):
		return self._sub.cost() + 20.0

	def description(self):
		return f'{self._sub.description()}, y salsa de tomate, y albóndigas'

def main():
	sub_classic = SubwayClassicDecorator()
	print(sub_classic.cost(), sub_classic.description())

	sub_chicken = SubwayChickenConcreteDecorator(sub_classic)
	print(sub_chicken.cost(), sub_chicken.description())

	sub_italian = SubwayItalianConcreteDecorator(sub_chicken)
	print(sub_italian.cost(), sub_italian.description())

if __name__ == '__main__':
	main()