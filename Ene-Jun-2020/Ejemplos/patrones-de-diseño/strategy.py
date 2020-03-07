import abc

class SortStrategy(metaclass=abc.ABCMeta):
	"""docstring for SortStrategy"""
	
	@abc.abstractmethod
	def sort(self):
		pass
		
class BubbleSortConcreteStrategy(SortStrategy):
	"""docstring for BubbleSortConcreteStrategy"""
	def sort(self):
		return 'Ordenando con bubble sort!'

class QuickSortConcreteStrategy(SortStrategy):
	"""docstring for QuickSortConcreteStrategy"""
	def sort(self):
		return 'Ordenando con quick sort!'

class SortContext(object):
	"""docstring for Contexto"""
	def __init__(self, my_list: list, strategy: SortStrategy = None):
		self._my_list = my_list
		self._strategy = strategy

	def sort_context(self):
		# Da la opción de que el cliente elija su propia estrategia
		if self._strategy != None:
			return self._strategy.sort()

		# En caso contrario, deja que el contexto determine la estrategia
		if len(self._my_list) < 100:
			return BubbleSortConcreteStrategy().sort()

		return QuickSortConcreteStrategy().sort()

	def set_strategy(self, strategy: SortStrategy):
		self._strategy = strategy

	def __str__(self):
		return f'Lista: {self._my_list}\nEstrategia: {self._strategy}'
		
def main():
	my_list = [i for i in range(0, 1000)]
	quick_sorter = QuickSortConcreteStrategy()
	context = SortContext(my_list)
	# print(context.sort_context())

	bubble_sorter = BubbleSortConcreteStrategy()
	context.set_strategy(bubble_sorter)
	# print(context.sort_context())
	
	print(context.sort_context())


if __name__ == '__main__':
	main()